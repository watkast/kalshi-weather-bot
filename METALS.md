# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:52 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 52 | 50 | 16 (32%) | 39¢ | 48% | -$44.67 | -22% |
| Silver | 26 | 25 | 7 (28%) | 34¢ | 43% | -$19.86 | -22% |
| Gold | 26 | 25 | 9 (36%) | 44¢ | 52% | -$24.81 | -22% |

*Earlier half $12.44 / later half -$57.11.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 51 | 13 (25%) | -$84.34 | -39% |
| 4¢+ ← live bot | 49 | 14 (29%) | -$43.25 | -24% |
| 6¢+ | 45 | 14 (31%) | -$9.23 | -6% |
| 8¢+ | 40 | 12 (30%) | $1.89 | +2% |
| 10¢+ | 33 | 8 (24%) | -$6.99 | -8% |
| 15¢+ | 17 | 5 (29%) | $14.03 | +39% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1255 | -7.5% |
| Hyperliquid price vs Kalshi's target | 1255 | -8.6% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:51:54 AM | Silver | UP | 8.1 min | 24¢ | 32% | 7¢ | Open | — |
| 9/29 3:47:14 AM | Gold | UP | 12.8 min | 61¢ | 69% | 6¢ | Open | — |
| 9/29 3:32:14 AM | Silver | DOWN | 12.8 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/29 3:31:07 AM | Gold | DOWN | 13.9 min | 47¢ | 56% | 7¢ | ❌ Lost | -$4.88 |
| 9/29 3:22:33 AM | Silver | UP | 7.5 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/29 3:16:18 AM | Gold | DOWN | 13.7 min | 39¢ | 50% | 9¢ | ❌ Lost | -$4.07 |
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/29 3:02:03 AM | Gold | DOWN | 12.9 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
| 9/29 12:33:04 AM | Gold | DOWN | 11.9 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 12:31:29 AM | Silver | DOWN | 13.5 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
