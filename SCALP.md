# Range-Scalp Bot

*Updated Fri Nov 13 04:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57831 | 50447 | 7384 (101) | 2 | $-15705.63 | -4.3% |
| **+10¢** | 43214 | 34591 | 8623 (133) | 5 | $-14628.52 | -5.4% |
| **+15¢** | 36230 | 26951 | 9279 (167) | 4 | $-13148.33 | -5.8% |
| **+20¢** | 32272 | 22534 | 9738 (217) | 7 | $-11521.92 | -5.7% |
| **+10¢ (15¢ stop)** | 70493 | 70365 | 128 (78) | 3 | $-25966.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 04:36 | +10 stop | BNB | UP | 0.65 | open |  |
| 11-13 04:36 | +20 | BNB | UP | 0.65 | open |  |
| 11-13 04:36 | +15 | BNB | UP | 0.66 | open |  |
| 11-13 04:36 | +10 | BNB | UP | 0.66 | open |  |
| 11-13 04:36 | +5 | BNB | UP | 0.65 | open |  |
| 11-13 04:35 | +10 stop | BTC | UP | 0.63 | open |  |
| 11-13 04:35 | +20 | BTC | UP | 0.63 | open |  |
| 11-13 04:35 | +15 | BTC | UP | 0.63 | open |  |
| 11-13 04:35 | +10 | BTC | UP | 0.63 | open |  |
| 11-13 04:35 | +5 | BTC | UP | 0.63 | open |  |
| 11-13 04:35 | +15 | DOGE | UP | 0.68 | open |  |
| 11-13 04:35 | +10 | DOGE | UP | 0.68 | open |  |
| 11-13 04:35 | +5 | DOGE | UP | 0.68 | 0.73 | 0.20 |
| 11-13 04:35 | +10 stop | NEAR | UP | 0.64 | open |  |
| 11-13 04:35 | +15 | NEAR | UP | 0.64 | open |  |
| 11-13 04:35 | +10 | NEAR | UP | 0.64 | open |  |
| 11-13 04:35 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 11-13 04:34 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-13 04:33 | +5 | ZEC | DOWN | 0.51 | 0.56 | 0.14 |
| 11-13 04:33 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 11-13 04:33 | +10 | ETH | UP | 0.67 | open |  |
| 11-13 04:33 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 11-13 04:33 | +5 | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 11-13 04:32 | +5 | ZEC | DOWN | 0.54 | 0.65 | 0.76 |
| 11-13 04:32 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-13 04:32 | +20 | NEAR | UP | 0.60 | open |  |
| 11-13 04:32 | +15 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-13 04:32 | +10 | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 11-13 04:32 | +5 | NEAR | UP | 0.60 | 0.67 | 0.37 |
| 11-13 04:32 | +10 stop | DOGE | UP | 0.67 | 0.78 | 0.81 |
| 11-13 04:32 | +5 | BNB | UP | 0.70 | 0.78 | 0.52 |
| 11-13 04:31 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-13 04:31 | +20 | BTC | UP | 0.64 | 0.84 | 1.73 |
| 11-13 04:31 | +15 | BTC | UP | 0.64 | 0.79 | 1.21 |
| 11-13 04:31 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-13 04:31 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-13 04:31 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-13 04:31 | +20 | ZEC | DOWN | 0.58 | open |  |
| 11-13 04:31 | +15 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-13 04:31 | +10 | ZEC | DOWN | 0.57 | 0.68 | 0.76 |
