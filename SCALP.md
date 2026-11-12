# Range-Scalp Bot

*Updated Thu Nov 12 11:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56846 | 49553 | 7293 (101) | 3 | $-15652.41 | -4.4% |
| **+10¢** | 42484 | 33977 | 8507 (133) | 4 | $-14575.65 | -5.5% |
| **+15¢** | 35620 | 26463 | 9157 (167) | 4 | $-13197.18 | -5.9% |
| **+20¢** | 31730 | 22122 | 9608 (217) | 4 | $-11584.22 | -5.8% |
| **+10¢ (15¢ stop)** | 69315 | 69187 | 128 (78) | 0 | $-25609.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 11:52 | +10 stop | SOL | UP | 0.32 | 0.53 | 1.76 |
| 11-12 11:51 | +10 stop | HYPE | DOWN | 0.53 | 0.78 | 2.19 |
| 11-12 11:51 | +10 stop | SOL | DOWN | 0.63 | 0.40 | -2.64 |
| 11-12 11:51 | +5 | SOL | DOWN | 0.64 | 0.90 | 2.39 |
| 11-12 11:51 | +5 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-12 11:50 | +5 | BTC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-12 11:50 | +10 stop | XRP | DOWN | 0.52 | 0.79 | 2.40 |
| 11-12 11:50 | +10 stop | DOGE | DOWN | 0.57 | 0.77 | 1.68 |
| 11-12 11:50 | +10 stop | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 11:50 | +20 | ZEC | DOWN | 0.57 | 0.84 | 2.42 |
| 11-12 11:50 | +15 | ZEC | DOWN | 0.57 | 0.84 | 2.42 |
| 11-12 11:50 | +10 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-12 11:50 | +5 | ZEC | DOWN | 0.57 | 0.65 | 0.46 |
| 11-12 11:50 | +10 stop | BTC | DOWN | 0.64 | 0.40 | -2.74 |
| 11-12 11:49 | +5 | SOL | UP | 0.48 | 0.63 | 1.15 |
| 11-12 11:49 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 11:49 | +20 | NEAR | DOWN | 0.64 | 0.92 | 2.58 |
| 11-12 11:49 | +15 | NEAR | DOWN | 0.64 | 0.92 | 2.58 |
| 11-12 11:49 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-12 11:49 | +5 | NEAR | DOWN | 0.65 | 0.74 | 0.60 |
| 11-12 11:49 | +10 | SOL | UP | 0.68 | open |  |
| 11-12 11:48 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 11-12 11:48 | +5 | ZEC | UP | 0.60 | 0.66 | 0.27 |
| 11-12 11:48 | +10 stop | HYPE | DOWN | 0.54 | 0.67 | 0.96 |
| 11-12 11:47 | +10 | SOL | UP | 0.48 | 0.60 | 0.83 |
| 11-12 11:47 | +5 | SOL | UP | 0.48 | 0.58 | 0.62 |
| 11-12 11:47 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-12 11:47 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 11-12 11:47 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-12 11:47 | +15 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-12 11:47 | +10 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-12 11:47 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 11-12 11:47 | +5 | DOGE | UP | 0.64 | open |  |
| 11-12 11:47 | +10 stop | BNB | DOWN | 0.63 | 0.47 | -1.95 |
| 11-12 11:47 | +20 | BNB | DOWN | 0.63 | 0.91 | 2.57 |
| 11-12 11:47 | +15 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 11-12 11:47 | +10 | BNB | DOWN | 0.63 | 0.79 | 1.31 |
| 11-12 11:47 | +5 | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 11-12 11:47 | +10 stop | XRP | UP | 0.64 | 0.47 | -2.05 |
| 11-12 11:47 | +20 | XRP | UP | 0.65 | open |  |
