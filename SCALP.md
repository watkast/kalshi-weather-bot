# Range-Scalp Bot

*Updated Sat Nov 21 14:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67461 | 58876 | 8585 (134) | 4 | $-18095.21 | -4.3% |
| **+10¢** | 50384 | 40354 | 10030 (175) | 3 | $-16793.70 | -5.3% |
| **+15¢** | 42252 | 31441 | 10811 (225) | 6 | $-15030.14 | -5.7% |
| **+20¢** | 37606 | 26246 | 11360 (283) | 7 | $-13344.73 | -5.7% |
| **+10¢ (15¢ stop)** | 82120 | 81949 | 171 (105) | 1 | $-30139.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 14:35 | +15 | BTC | UP | 0.44 | 0.60 | 1.25 |
| 11-21 14:35 | +10 | BTC | UP | 0.44 | 0.60 | 1.25 |
| 11-21 14:35 | +10 stop | HYPE | UP | 0.40 | 0.54 | 1.01 |
| 11-21 14:35 | +10 | HYPE | UP | 0.43 | 0.54 | 0.75 |
| 11-21 14:35 | +10 stop | BTC | UP | 0.68 | 0.40 | -3.13 |
| 11-21 14:35 | +5 | BTC | UP | 0.67 | open |  |
| 11-21 14:35 | +10 stop | ZEC | UP | 0.70 | open |  |
| 11-21 14:35 | +10 stop | BNB | UP | 0.65 | 0.43 | -2.54 |
| 11-21 14:35 | +20 | BNB | UP | 0.65 | open |  |
| 11-21 14:35 | +15 | BNB | UP | 0.65 | open |  |
| 11-21 14:35 | +10 | BNB | UP | 0.65 | open |  |
| 11-21 14:35 | +5 | BNB | UP | 0.65 | open |  |
| 11-21 14:35 | +10 stop | XRP | DOWN | 0.60 | 0.83 | 2.03 |
| 11-21 14:35 | +15 | XRP | DOWN | 0.60 | 0.83 | 2.03 |
| 11-21 14:35 | +10 | XRP | DOWN | 0.60 | 0.83 | 2.03 |
| 11-21 14:35 | +5 | XRP | DOWN | 0.61 | 0.68 | 0.37 |
| 11-21 14:34 | +10 stop | HYPE | DOWN | 0.48 | 0.60 | 0.85 |
| 11-21 14:34 | +10 | HYPE | DOWN | 0.48 | 0.60 | 0.85 |
| 11-21 14:33 | +10 stop | BTC | DOWN | 0.66 | 0.39 | -3.03 |
| 11-21 14:33 | +10 stop | ZEC | DOWN | 0.64 | 0.40 | -2.74 |
| 11-21 14:33 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-21 14:33 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-21 14:33 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 11-21 14:33 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-21 14:33 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-21 14:33 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-21 14:33 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-21 14:33 | +5 | HYPE | DOWN | 0.71 | open |  |
| 11-21 14:33 | +10 stop | DOGE | DOWN | 0.65 | 0.44 | -2.44 |
| 11-21 14:33 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-21 14:33 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-21 14:33 | +10 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 14:33 | +5 | DOGE | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 14:33 | +10 stop | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-21 14:33 | +20 | ETH | DOWN | 0.64 | open |  |
| 11-21 14:33 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-21 14:33 | +10 | ETH | DOWN | 0.64 | 0.76 | 0.90 |
| 11-21 14:33 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 11-21 14:32 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 11-21 14:32 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
