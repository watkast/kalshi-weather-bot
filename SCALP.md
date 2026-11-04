# Range-Scalp Bot

*Updated Wed Nov 04 12:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47237 | 41136 | 6101 (72) | 4 | $-13586.24 | -4.6% |
| **+10¢** | 35285 | 28206 | 7079 (97) | 5 | $-12428.52 | -5.6% |
| **+15¢** | 29547 | 21925 | 7622 (125) | 5 | $-11397.48 | -6.1% |
| **+20¢** | 26250 | 18267 | 7983 (165) | 5 | $-10056.48 | -6.1% |
| **+10¢ (15¢ stop)** | 57584 | 57491 | 93 (56) | 0 | $-21477.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 12:27 | +10 stop | HYPE | DOWN | 0.63 | 0.93 | 2.80 |
| 11-04 12:25 | +10 stop | HYPE | DOWN | 0.62 | 0.37 | -2.84 |
| 11-04 12:25 | +10 | HYPE | DOWN | 0.62 | 0.93 | 2.90 |
| 11-04 12:25 | +5 | HYPE | DOWN | 0.62 | 0.93 | 2.90 |
| 11-04 12:24 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-04 12:22 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-04 12:22 | +10 | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 11-04 12:22 | +5 | DOGE | UP | 0.65 | 0.71 | 0.29 |
| 11-04 12:22 | +10 stop | XRP | DOWN | 0.62 | 0.45 | -2.05 |
| 11-04 12:22 | +10 stop | HYPE | UP | 0.47 | 0.60 | 0.95 |
| 11-04 12:21 | +10 stop | XRP | UP | 0.44 | 0.63 | 1.55 |
| 11-04 12:17 | +10 stop | ETH | UP | 0.60 | 0.77 | 1.40 |
| 11-04 12:17 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-04 12:17 | +20 | ZEC | UP | 0.63 | 0.83 | 1.73 |
| 11-04 12:17 | +15 | ZEC | UP | 0.63 | 0.78 | 1.20 |
| 11-04 12:17 | +10 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-04 12:17 | +5 | ZEC | UP | 0.62 | 0.73 | 0.79 |
| 11-04 12:17 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-04 12:17 | +10 stop | BNB | UP | 0.62 | 0.75 | 0.99 |
| 11-04 12:16 | +10 stop | SOL | UP | 0.65 | 0.77 | 0.91 |
| 11-04 12:16 | +10 stop | XRP | UP | 0.65 | 0.76 | 0.81 |
| 11-04 12:16 | +10 stop | HYPE | UP | 0.52 | 0.73 | 1.78 |
| 11-04 12:16 | +10 stop | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-04 12:16 | +20 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-04 12:16 | +15 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 11-04 12:16 | +10 | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-04 12:16 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 11-04 12:15 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.84 |
| 11-04 12:15 | +20 | HYPE | DOWN | 0.68 | 0.93 | 2.31 |
| 11-04 12:15 | +15 | HYPE | DOWN | 0.68 | 0.93 | 2.35 |
| 11-04 12:15 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 12:15 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 12:15 | +10 stop | NEAR | DOWN | 0.59 | 0.31 | -3.12 |
| 11-04 12:15 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-04 12:15 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-04 12:15 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-04 12:15 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 11-04 12:15 | +10 stop | BNB | DOWN | 0.62 | 0.31 | -3.42 |
| 11-04 12:15 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-04 12:15 | +15 | BNB | DOWN | 0.62 | open |  |
