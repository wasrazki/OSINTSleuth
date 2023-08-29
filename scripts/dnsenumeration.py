import dns.resolver

record_types =[ 'A', 'AAAA', 'NS', 'CNAME', 'MX', 'TXT', 'SOA', 'PTR']

def enumerate_record_types (domain):
    output=""
    for record in record_types:
        
        try:
            answer= dns.resolver.resolve(domain, record)
            output += f'{"-" * 40}\n{record} Records :\n' 
            for server in answer:
                output += server.to_text() + '\n' 
        except dns.resolver.NoAnswer:
            pass 
        except dns.resolver.LifetimeTimeout: 
            pass
        except KeyboardInterrupt: 
            quit()
        except dns.resolver.NXDOMAIN:
            print (f'{domain} Does not exist')
            quit()
    return output
"""
if __name__ == '__main__':
   ho =  enumerate_record_types("facebook.com")
   print(ho)"""