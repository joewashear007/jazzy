export module jazzy {
   module Structure {
    export class HashTable<T>{
      private _table : Object;

      constructor(){
        this._table = new Object();
      }

      public Contains(name:string): boolean {
        return this._table.hasOwnProperty(name);
      }

      public Get(name:string): T{
        return this._table[name];
      }

      public Set(name:string, value:T):void{
        this._table[name] = value;
      }
    }
  }
}
