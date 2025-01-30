def main():
    
    import sys
    import os
    sys.path.append(os.getcwd())

    import path
    path.path=os.getcwd()

    import log
    log.log=log.create_log()

    try:
        
        import tk
        tk.create_tk()
        
    except Exception as error:
        
        tk.data.error=error
        if tk.data.test:
            raise error
        
    else:
        
        if tk.data.error:
            raise tk.data.error
        
    finally:
        
        if tk.data.error:
            log.log.record("f'{data.error}'",log.logging.ERROR)
        log.log.close()

if __name__=='__main__':

    main()
