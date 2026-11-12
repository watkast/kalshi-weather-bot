# Range-Scalp Bot

*Updated Thu Nov 12 15:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57092 | 49770 | 7322 (101) | 1 | $-15701.68 | -4.4% |
| **+10¢** | 42673 | 34131 | 8542 (133) | 2 | $-14628.81 | -5.5% |
| **+15¢** | 35777 | 26584 | 9193 (167) | 2 | $-13216.51 | -5.9% |
| **+20¢** | 31873 | 22228 | 9645 (217) | 4 | $-11579.39 | -5.8% |
| **+10¢ (15¢ stop)** | 69625 | 69497 | 128 (78) | 0 | $-25714.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 15:37 | +10 stop | XRP | DOWN | 0.70 | 0.50 | -2.33 |
| 11-12 15:37 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-12 15:37 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-12 15:37 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-12 15:37 | +10 stop | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 11-12 15:37 | +5 | DOGE | UP | 0.57 | 0.65 | 0.46 |
| 11-12 15:34 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 15:33 | +10 stop | DOGE | DOWN | 0.62 | 0.73 | 0.79 |
| 11-12 15:32 | +5 | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 11-12 15:32 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 15:32 | +5 | ETH | DOWN | 0.69 | 0.77 | 0.52 |
| 11-12 15:32 | +10 stop | DOGE | DOWN | 0.53 | 0.67 | 1.02 |
| 11-12 15:32 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-12 15:31 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-12 15:31 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 11-12 15:31 | +15 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-12 15:31 | +10 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-12 15:31 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 11-12 15:31 | +10 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-12 15:31 | +5 | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 11-12 15:31 | +10 stop | BTC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-12 15:31 | +20 | BTC | DOWN | 0.58 | 0.81 | 2.01 |
| 11-12 15:31 | +15 | BTC | DOWN | 0.57 | 0.74 | 1.38 |
| 11-12 15:31 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 15:31 | +5 | BTC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-12 15:31 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 15:31 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-12 15:31 | +15 | XRP | DOWN | 0.71 | 0.86 | 1.26 |
| 11-12 15:31 | +10 stop | DOGE | DOWN | 0.64 | 0.46 | -2.15 |
| 11-12 15:31 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-12 15:31 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-12 15:31 | +10 | DOGE | DOWN | 0.64 | open |  |
| 11-12 15:31 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-12 15:31 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 15:31 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-12 15:31 | +15 | NEAR | DOWN | 0.69 | 0.86 | 1.46 |
| 11-12 15:31 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 11-12 15:31 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 11-12 15:31 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-12 15:31 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
