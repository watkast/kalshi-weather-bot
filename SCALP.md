# Range-Scalp Bot

*Updated Fri Nov 13 12:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58284 | 50860 | 7424 (102) | 2 | $-15705.20 | -4.3% |
| **+10¢** | 43555 | 34874 | 8681 (134) | 3 | $-14669.05 | -5.4% |
| **+15¢** | 36514 | 27167 | 9347 (169) | 3 | $-13215.25 | -5.8% |
| **+20¢** | 32529 | 22713 | 9816 (220) | 4 | $-11615.61 | -5.7% |
| **+10¢ (15¢ stop)** | 71017 | 70888 | 129 (79) | 2 | $-26112.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 12:37 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-13 12:37 | +20 | ETH | UP | 0.56 | open |  |
| 11-13 12:37 | +15 | ETH | UP | 0.56 | open |  |
| 11-13 12:37 | +10 | ETH | UP | 0.56 | open |  |
| 11-13 12:37 | +5 | ETH | UP | 0.58 | 0.63 | 0.15 |
| 11-13 12:37 | +10 stop | DOGE | DOWN | 0.71 | open |  |
| 11-13 12:35 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-13 12:34 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 11-13 12:34 | +15 | DOGE | UP | 0.65 | open |  |
| 11-13 12:34 | +10 | DOGE | UP | 0.65 | open |  |
| 11-13 12:34 | +5 | DOGE | UP | 0.65 | open |  |
| 11-13 12:33 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 11-13 12:33 | +10 | XRP | UP | 0.58 | open |  |
| 11-13 12:33 | +5 | XRP | UP | 0.58 | open |  |
| 11-13 12:32 | +5 | XRP | UP | 0.66 | 0.74 | 0.50 |
| 11-13 12:32 | +10 stop | NEAR | UP | 0.65 | 0.78 | 1.03 |
| 11-13 12:32 | +20 | NEAR | UP | 0.65 | 0.86 | 1.87 |
| 11-13 12:32 | +15 | NEAR | UP | 0.66 | 0.81 | 1.23 |
| 11-13 12:32 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-13 12:32 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-13 12:31 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-13 12:31 | +20 | XRP | UP | 0.63 | open |  |
| 11-13 12:31 | +15 | XRP | UP | 0.63 | open |  |
| 11-13 12:31 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-13 12:31 | +5 | XRP | UP | 0.63 | 0.71 | 0.48 |
| 11-13 12:31 | +10 stop | BNB | UP | 0.70 | 0.87 | 1.47 |
| 11-13 12:31 | +20 | BNB | UP | 0.70 | open |  |
| 11-13 12:31 | +15 | BNB | UP | 0.70 | 0.87 | 1.47 |
| 11-13 12:31 | +10 | BNB | UP | 0.70 | 0.87 | 1.47 |
| 11-13 12:31 | +5 | BNB | UP | 0.70 | 0.87 | 1.47 |
| 11-13 12:31 | +10 stop | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 11-13 12:31 | +20 | DOGE | UP | 0.64 | open |  |
| 11-13 12:31 | +15 | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-13 12:31 | +10 | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 11-13 12:31 | +5 | DOGE | UP | 0.64 | 0.77 | 1.00 |
| 11-13 12:27 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 11-13 12:27 | +10 stop | HYPE | DOWN | 0.71 | 0.84 | 1.09 |
| 11-13 12:27 | +20 | HYPE | DOWN | 0.70 | 0.90 | 1.81 |
| 11-13 12:27 | +15 | HYPE | DOWN | 0.70 | 0.90 | 1.81 |
| 11-13 12:27 | +10 | HYPE | DOWN | 0.70 | 0.84 | 1.15 |
