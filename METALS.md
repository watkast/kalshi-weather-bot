# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:11 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 40 | 38 | 15 (39%) | 41¢ | 49% | -$11.70 | -7% |
| Silver | 20 | 19 | 6 (32%) | 35¢ | 44% | -$9.27 | -13% |
| Gold | 20 | 19 | 9 (47%) | 47¢ | 55% | -$2.43 | -3% |

*Earlier half $17.14 / later half -$28.84.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 38 | 12 (32%) | -$46.39 | -28% |
| 4¢+ ← live bot | 37 | 13 (35%) | -$9.23 | -7% |
| 6¢+ | 35 | 12 (34%) | $4.91 | +4% |
| 8¢+ | 32 | 12 (38%) | $26.28 | +28% |
| 10¢+ | 28 | 8 (29%) | $7.37 | +10% |
| 15¢+ | 14 | 5 (36%) | $18.25 | +57% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 949 | -5.0% |
| Hyperliquid price vs Kalshi's target | 949 | -11.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | Open | — |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | Open | — |
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | ❌ Lost | -$3.46 |
| 9/28 11:34:38 PM | Silver | DOWN | 10.4 min | 81¢ | 92% | 10¢ | ❌ Lost | -$8.21 |
| 9/28 11:31:34 PM | Gold | DOWN | 13.4 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | ✅ Won | $7.05 |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
| 9/28 10:52:13 PM | Silver | DOWN | 7.8 min | 45¢ | 52% | 5¢ | ✅ Won | $5.32 |
| 9/28 10:47:04 PM | Gold | UP | 12.9 min | 52¢ | 59% | 5¢ | ❌ Lost | -$5.38 |
