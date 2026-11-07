# Range-Scalp Bot

*Updated Sat Nov 07 20:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51445 | 44855 | 6590 (80) | 0 | $-14290.98 | -4.4% |
| **+10¢** | 38391 | 30709 | 7682 (106) | 0 | $-13287.29 | -5.5% |
| **+15¢** | 32140 | 23861 | 8279 (135) | 0 | $-12194.70 | -6.0% |
| **+20¢** | 28586 | 19908 | 8678 (178) | 0 | $-10758.22 | -6.0% |
| **+10¢ (15¢ stop)** | 62646 | 62543 | 103 (61) | 0 | $-23171.71 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 19:57 | +10 stop | NEAR | UP | 0.37 | 0.52 | 1.15 |
| 11-07 19:55 | +10 stop | NEAR | DOWN | 0.61 | 0.39 | -2.54 |
| 11-07 19:55 | +10 stop | ZEC | DOWN | 0.71 | 0.42 | -3.23 |
| 11-07 19:54 | +10 stop | NEAR | DOWN | 0.70 | 0.54 | -1.93 |
| 11-07 19:54 | +15 | NEAR | DOWN | 0.70 | no | 2.85 |
| 11-07 19:54 | +10 | NEAR | DOWN | 0.70 | no | 2.85 |
| 11-07 19:54 | +5 | NEAR | DOWN | 0.70 | no | 2.85 |
| 11-07 19:53 | +5 | BTC | UP | 0.65 | 0.70 | 0.19 |
| 11-07 19:53 | +10 stop | HYPE | DOWN | 0.65 | 0.49 | -1.94 |
| 11-07 19:53 | +10 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 11-07 19:53 | +5 | HYPE | DOWN | 0.65 | yes | -6.66 |
| 11-07 19:52 | +10 stop | SOL | UP | 0.60 | 0.78 | 1.50 |
| 11-07 19:52 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 11-07 19:51 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-07 19:51 | +20 | DOGE | UP | 0.62 | 0.86 | 2.14 |
| 11-07 19:51 | +15 | DOGE | UP | 0.62 | 0.86 | 2.14 |
| 11-07 19:51 | +10 | DOGE | UP | 0.62 | 0.73 | 0.81 |
| 11-07 19:51 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 11-07 19:51 | +10 stop | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-07 19:51 | +15 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-07 19:51 | +10 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-07 19:51 | +5 | BNB | UP | 0.62 | 0.81 | 1.62 |
| 11-07 19:51 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-07 19:51 | +5 | ETH | UP | 0.63 | 0.69 | 0.28 |
| 11-07 19:51 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-07 19:49 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-07 19:49 | +10 stop | SOL | UP | 0.69 | 0.49 | -2.30 |
| 11-07 19:49 | +10 | SOL | UP | 0.69 | 0.84 | 1.28 |
| 11-07 19:49 | +5 | SOL | UP | 0.69 | 0.78 | 0.65 |
| 11-07 19:49 | +10 stop | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-07 19:49 | +10 | BTC | UP | 0.66 | 0.77 | 0.81 |
| 11-07 19:49 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-07 19:49 | +10 stop | ETH | UP | 0.68 | 0.82 | 1.13 |
| 11-07 19:49 | +15 | ETH | UP | 0.68 | 0.91 | 2.08 |
| 11-07 19:49 | +10 | ETH | UP | 0.68 | 0.82 | 1.13 |
| 11-07 19:49 | +5 | ETH | UP | 0.68 | 0.74 | 0.30 |
| 11-07 19:49 | +10 stop | XRP | UP | 0.62 | 0.45 | -2.05 |
| 11-07 19:49 | +20 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 11-07 19:49 | +15 | XRP | UP | 0.62 | 0.85 | 2.04 |
| 11-07 19:49 | +10 | XRP | UP | 0.62 | 0.73 | 0.79 |
