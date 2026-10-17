# Range-Scalp Bot

*Updated Sat Oct 17 10:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20789 | 18085 | 2704 (29) | 0 | $-6124.09 | -4.7% |
| **+10¢** | 15661 | 12546 | 3115 (41) | 0 | $-5418.82 | -5.5% |
| **+15¢** | 13095 | 9743 | 3352 (61) | 0 | $-4887.49 | -5.9% |
| **+20¢** | 11605 | 8095 | 3510 (80) | 0 | $-4321.49 | -5.9% |
| **+10¢ (15¢ stop)** | 25559 | 25509 | 50 (29) | 0 | $-9747.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 10:05 | +10 stop | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-17 10:05 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 10-17 10:05 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-17 10:05 | +10 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 10-17 10:05 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 10-17 09:58 | +10 stop | HYPE | UP | 0.59 | 0.44 | -1.85 |
| 10-17 09:58 | +20 | HYPE | UP | 0.59 | no | -6.07 |
| 10-17 09:58 | +15 | HYPE | UP | 0.59 | no | -6.07 |
| 10-17 09:58 | +10 | HYPE | UP | 0.59 | no | -6.07 |
| 10-17 09:58 | +5 | HYPE | UP | 0.59 | no | -6.07 |
| 10-17 09:57 | +10 stop | SOL | UP | 0.65 | 0.41 | -2.73 |
| 10-17 09:50 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-17 09:50 | +5 | HYPE | UP | 0.68 | 0.77 | 0.61 |
| 10-17 09:49 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-17 09:49 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 10-17 09:49 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-17 09:49 | +10 stop | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-17 09:49 | +15 | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-17 09:49 | +10 | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-17 09:49 | +5 | HYPE | UP | 0.59 | 0.65 | 0.27 |
| 10-17 09:49 | +10 stop | SOL | UP | 0.67 | 0.82 | 1.23 |
| 10-17 09:48 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-17 09:48 | +5 | BTC | DOWN | 0.64 | 0.99 | 3.32 |
| 10-17 09:48 | +10 stop | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-17 09:48 | +10 stop | DOGE | DOWN | 0.62 | 0.47 | -1.85 |
| 10-17 09:48 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.77 |
| 10-17 09:47 | +10 stop | SOL | UP | 0.69 | 0.44 | -2.83 |
| 10-17 09:47 | +15 | DOGE | UP | 0.65 | 0.81 | 1.33 |
| 10-17 09:47 | +20 | XRP | UP | 0.64 | 0.84 | 1.73 |
| 10-17 09:47 | +10 stop | DOGE | UP | 0.66 | 0.40 | -2.93 |
| 10-17 09:47 | +10 | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 10-17 09:47 | +5 | DOGE | UP | 0.66 | 0.72 | 0.29 |
| 10-17 09:47 | +5 | ZEC | UP | 0.66 | 0.72 | 0.29 |
| 10-17 09:47 | +15 | XRP | UP | 0.63 | 0.78 | 1.20 |
| 10-17 09:47 | +10 stop | BNB | UP | 0.68 | 0.50 | -2.14 |
| 10-17 09:47 | +10 | BNB | UP | 0.68 | 0.80 | 0.92 |
| 10-17 09:47 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 10-17 09:47 | +10 stop | XRP | UP | 0.68 | 0.45 | -2.64 |
| 10-17 09:47 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 10-17 09:47 | +5 | XRP | UP | 0.68 | 0.78 | 0.71 |
