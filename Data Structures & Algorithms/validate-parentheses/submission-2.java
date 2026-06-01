class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for(char c : s.toCharArray()){
            
            switch(c){
                case '[':
                    stack.push(']');
                    break;
                case '{':
                    stack.push('}');
                    break;
                case '(':
                    stack.push(')');
                    break;
                case ']':
                    if(!stack.isEmpty() && stack.peek() == ']') stack.pop();
                    else return false;
                    break;
                case '}':
                    if(!stack.isEmpty() && stack.peek() == '}') stack.pop();
                    else return false;
                    break;
                case ')':
                    if(!stack.isEmpty() && stack.peek() == ')') stack.pop();
                    else return false;
                    break;
            }
                
        }
        return stack.isEmpty();
    }
}
