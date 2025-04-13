require "csv"
require "optparse"
require "json"

def analyze_inkscape_csv()
  baseline_csv = CSV.open("experiment/inkscape/baseline.csv", headers: true, header_converters: :symbol).to_a.map(&:to_hash)
  files = [
    "0_1_inkscape.csv",
    "2_0_inkscape.csv",
    "3_0_inkscape.csv",
    "3_1_inkscape.csv",
    "4_0_inkscape.csv",
    "4_1_inkscape.csv",
    "6_0_inkscape.csv",
    "6_1_inkscape.csv"
  ]

  graves_processed = {}

  errors = files.map do |file|
    data = CSV.open("experiment/inkscape/#{file}", headers: true, header_converters: :symbol).to_a.map(&:to_hash)

    grave_count = data.count { |user| !user[:length_px]&.empty? && !user[:length_px].nil? }
    graves_processed[file] = grave_count

    combined_data = baseline_csv.zip(data)
    combined_data = combined_data.filter { |base, user| !base.empty? && !user.empty? }

    total_error = get_inkscape_error(combined_data)

    [file, total_error]
  end.to_h

  File.open('output/errors_inkscape.json', 'w') do |f|
    f.write(errors.to_json)
  end

  CSV.open("output/inkscape_count.csv", "w") do |csv|
    csv << ["User", "Graves"]
    graves_processed.each do |user, count|
      csv << [user, count]
    end
  end
end

def analyze_comove_csv()
  base_path = "experiment/comove/baseline.csv"
  baseline_csv = CSV.open(base_path, headers: true, header_converters: :symbol).to_a.map(&:to_hash)
  files = [
    "0_1.csv",
    "2_0.csv",
    "3_0.csv",
    "3_1.csv",
    "4_0.csv",
    "4_1.csv",
    "5_0.csv",
    "5_1.csv",
    "6_0.csv",
    "6_1.csv"
  ]

  graves_processed = {}
  errors = files.map do |file|
    data = CSV.open("experiment/comove/#{file}", headers: true, header_converters: :symbol).to_a.map(&:to_hash)
    combined_data = baseline_csv.zip(data)

    grave_count = data.count
    graves_processed[file] = grave_count

    combined_data = combined_data.filter { |base, user| !base.empty? && !user.nil? && !user.empty? }
    total_error = get_error(combined_data)
    [file, total_error]
  end.to_h

  File.open('output/errors_comove.json', 'w') do |f|
    f.write(errors.to_json)
  end

  CSV.open("output/comove_count.csv", "w") do |csv|
    csv << ["User", "Graves"]
    graves_processed.each do |user, count|
      csv << [user, count]
    end
  end
end

def get_inkscape_error(combined_data)
  combined_data.map do |base, user|
    if user[:length_m] == "#DIV/0!" || user[:width_m] == "#DIV/0!" || user[:depth_m] == "#DIV/0!"
      nil
    else
      difference = [
        (base[:length_m].to_f - (user[:length_m].to_f / 100)) / base[:length_m].to_f,
        (base[:width_m].to_f - (user[:width_m].to_f / 100)) / base[:width_m].to_f,
        (base[:depth_m].to_f - (user[:depth_m].to_f / 100)) / (base[:depth_m].to_f)
      ].compact.map(&:abs)

      if base[:depth_m].nil?
        difference[2] = 0
      end

      difference.sum(0.0) / difference.size
    end
  end.compact
end

def get_error(combined_data)
  combined_data.map do |base, user|
    difference = base.map do |key, _value|
      if %i[id updated_at].include?(key)
        nil
      else
        base_value = base[key].to_f
        user_value = user[key].to_f
        if base_value.zero?
          if user_value.zero?
            0
          else
            1
          end
        else
          diff = base_value - user_value
          diff / base_value
        end
      end
    end.compact.map(&:abs)
    difference.sum(0.0) / difference.size
  end
end

analyze_comove_csv()
analyze_inkscape_csv()
