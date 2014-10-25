#birdsong.rb
require 'net/https'
require 'clockwork'
 
api = Clockwork::API.new('6f7e73dd28bf6022c1a988a884c880f283830ece')
message = api.messages.build( :to => '447731090123', :content => 'Test text' )
response = message.deliver
 
if response.success
    puts response.message_id
else
    puts response.error_code
    puts response.error_description
end


