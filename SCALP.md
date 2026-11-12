# Range-Scalp Bot

*Updated Thu Nov 12 11:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56814 | 49524 | 7290 (101) | 3 | $-15658.00 | -4.4% |
| **+10¢** | 42458 | 33955 | 8503 (133) | 5 | $-14576.01 | -5.5% |
| **+15¢** | 35598 | 26445 | 9153 (167) | 4 | $-13206.67 | -5.9% |
| **+20¢** | 31709 | 22105 | 9604 (217) | 4 | $-11596.57 | -5.8% |
| **+10¢ (15¢ stop)** | 69283 | 69155 | 128 (78) | 0 | $-25614.41 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 11:10 | +10 stop | ETH | UP | 0.51 | 0.64 | 0.92 |
| 11-12 11:10 | +10 stop | NEAR | UP | 0.68 | 0.84 | 1.34 |
| 11-12 11:10 | +5 | NEAR | UP | 0.68 | 0.75 | 0.40 |
| 11-12 11:08 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 11:08 | +10 stop | ETH | DOWN | 0.69 | 0.51 | -2.13 |
| 11-12 11:08 | +10 stop | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-12 11:08 | +20 | SOL | UP | 0.69 | 0.91 | 1.96 |
| 11-12 11:08 | +15 | SOL | UP | 0.69 | 0.86 | 1.46 |
| 11-12 11:08 | +10 | SOL | UP | 0.69 | 0.79 | 0.73 |
| 11-12 11:08 | +5 | SOL | UP | 0.69 | 0.78 | 0.62 |
| 11-12 11:08 | +10 stop | BNB | DOWN | 0.49 | 0.63 | 1.05 |
| 11-12 11:06 | +10 stop | XRP | UP | 0.52 | 0.29 | -2.63 |
| 11-12 11:06 | +10 stop | BNB | DOWN | 0.49 | 0.60 | 0.76 |
| 11-12 11:06 | +10 stop | ETH | UP | 0.66 | 0.35 | -3.42 |
| 11-12 11:06 | +20 | ETH | UP | 0.66 | open |  |
| 11-12 11:06 | +15 | ETH | UP | 0.66 | open |  |
| 11-12 11:06 | +10 | ETH | UP | 0.66 | open |  |
| 11-12 11:06 | +5 | ETH | UP | 0.65 | 0.72 | 0.39 |
| 11-12 11:06 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 11-12 11:05 | +10 stop | BTC | DOWN | 0.70 | 0.52 | -2.13 |
| 11-12 11:05 | +10 stop | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-12 11:05 | +20 | SOL | UP | 0.54 | 0.76 | 1.89 |
| 11-12 11:05 | +15 | SOL | UP | 0.54 | 0.71 | 1.37 |
| 11-12 11:05 | +10 | SOL | UP | 0.54 | 0.67 | 0.96 |
| 11-12 11:05 | +5 | SOL | UP | 0.54 | 0.60 | 0.25 |
| 11-12 11:04 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-12 11:03 | +10 stop | BTC | UP | 0.51 | 0.36 | -1.85 |
| 11-12 11:03 | +20 | BTC | UP | 0.51 | open |  |
| 11-12 11:03 | +15 | BTC | UP | 0.51 | open |  |
| 11-12 11:03 | +10 | BTC | UP | 0.51 | open |  |
| 11-12 11:03 | +5 | BTC | UP | 0.51 | open |  |
| 11-12 11:03 | +10 stop | NEAR | DOWN | 0.71 | 0.50 | -2.43 |
| 11-12 11:03 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-12 11:03 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-12 11:02 | +15 | DOGE | UP | 0.63 | 0.79 | 1.31 |
| 11-12 11:02 | +10 stop | BNB | UP | 0.56 | 0.30 | -2.93 |
| 11-12 11:02 | +10 | BNB | UP | 0.57 | open |  |
| 11-12 11:02 | +10 stop | DOGE | UP | 0.63 | 0.46 | -2.05 |
| 11-12 11:02 | +10 | DOGE | UP | 0.63 | 0.77 | 1.10 |
| 11-12 11:02 | +5 | DOGE | UP | 0.63 | 0.69 | 0.28 |
