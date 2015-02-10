export module jazzy {
   export module Structure {
    export class StackList<T>{
      private _stack: Array<T>

      constructor(){
        this._stack = new Array<T>();
      }
      public Pop():T {
        // splice(x,y,z) : removes y elements and inserts z elements at x and
        return this._stack.splice(0,1)[0];
      }
      public Push(item: T):void {
        // splice(x,y) : removes y elements at x and returns them
        this._stack.splice(0,0,item);
      }
      public Get(i:number):T{
        // returns item or underfined;
        return this._stack[i];
      }
    }
  }
}
