# Range-Scalp Bot

*Updated Sat Nov 21 18:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67694 | 59080 | 8614 (134) | 1 | $-18187.02 | -4.3% |
| **+10¢** | 50546 | 40483 | 10063 (175) | 1 | $-16872.15 | -5.3% |
| **+15¢** | 42377 | 31529 | 10848 (225) | 0 | $-15115.31 | -5.7% |
| **+20¢** | 37717 | 26318 | 11399 (283) | 1 | $-13433.30 | -5.7% |
| **+10¢ (15¢ stop)** | 82397 | 82226 | 171 (105) | 0 | $-30232.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 17:59 | +10 stop | NEAR | UP | 0.47 | 0.67 | 1.62 |
| 11-21 17:56 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.91 |
| 11-21 17:56 | +10 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 17:56 | +5 | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 17:55 | +10 stop | HYPE | UP | 0.65 | 0.39 | -2.93 |
| 11-21 17:55 | +5 | HYPE | UP | 0.65 | open |  |
| 11-21 17:55 | +10 stop | SOL | DOWN | 0.56 | 0.66 | 0.67 |
| 11-21 17:54 | +10 stop | HYPE | UP | 0.55 | 0.37 | -2.15 |
| 11-21 17:54 | +10 stop | ETH | UP | 0.62 | 0.79 | 1.41 |
| 11-21 17:54 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 11-21 17:53 | +10 stop | SOL | UP | 0.53 | 0.37 | -1.95 |
| 11-21 17:53 | +10 stop | DOGE | DOWN | 0.61 | 0.74 | 0.99 |
| 11-21 17:53 | +15 | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 11-21 17:53 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-21 17:53 | +5 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-21 17:52 | +5 | HYPE | DOWN | 0.54 | 0.62 | 0.45 |
| 11-21 17:52 | +10 stop | BNB | DOWN | 0.68 | 0.82 | 1.12 |
| 11-21 17:52 | +15 | BNB | DOWN | 0.68 | 0.93 | 2.31 |
| 11-21 17:52 | +10 | BNB | DOWN | 0.68 | 0.82 | 1.12 |
| 11-21 17:52 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.50 |
| 11-21 17:52 | +10 stop | SOL | DOWN | 0.60 | 0.44 | -1.95 |
| 11-21 17:52 | +15 | SOL | DOWN | 0.60 | 0.89 | 2.66 |
| 11-21 17:52 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-21 17:52 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-21 17:52 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 11-21 17:52 | +15 | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-21 17:52 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 11-21 17:52 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.34 |
| 11-21 17:51 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-21 17:50 | +5 | XRP | DOWN | 0.58 | 0.65 | 0.36 |
| 11-21 17:49 | +10 stop | ETH | DOWN | 0.68 | 0.51 | -2.04 |
| 11-21 17:49 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-21 17:49 | +5 | ETH | DOWN | 0.67 | 0.72 | 0.19 |
| 11-21 17:49 | +5 | SOL | DOWN | 0.71 | 0.79 | 0.53 |
| 11-21 17:48 | +5 | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 11-21 17:47 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-21 17:47 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 11-21 17:47 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 11-21 17:46 | +5 | DOGE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-21 17:46 | +10 stop | XRP | DOWN | 0.57 | 0.67 | 0.66 |
