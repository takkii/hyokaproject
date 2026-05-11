begin
  require 'search.o'
rescue Exception => e
  puts e.backtrace
ensure
  GC.auto_compact
end

__END__
