# Range-Scalp Bot

*Updated Thu Nov 19 01:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64533 | 56292 | 8241 (124) | 0 | $-17561.15 | -4.3% |
| **+10¢** | 48212 | 38575 | 9637 (165) | 0 | $-16363.92 | -5.4% |
| **+15¢** | 40431 | 30044 | 10387 (210) | 0 | $-14767.33 | -5.8% |
| **+20¢** | 36006 | 25102 | 10904 (265) | 0 | $-13051.43 | -5.8% |
| **+10¢ (15¢ stop)** | 78543 | 78379 | 164 (98) | 0 | $-28892.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 01:12 | +10 stop | HYPE | DOWN | 0.68 | 0.27 | -4.36 |
| 11-19 01:12 | +10 stop | ETH | UP | 0.59 | 0.80 | 1.81 |
| 11-19 01:12 | +10 stop | BNB | UP | 0.71 | 0.48 | -2.63 |
| 11-19 01:11 | +10 stop | BNB | UP | 0.67 | 0.79 | 0.97 |
| 11-19 01:11 | +20 | BNB | UP | 0.67 | 0.95 | 2.63 |
| 11-19 01:11 | +15 | BNB | UP | 0.67 | 0.95 | 2.63 |
| 11-19 01:11 | +10 stop | HYPE | UP | 0.68 | 0.52 | -1.94 |
| 11-19 01:10 | +10 stop | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +15 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +10 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +5 | BTC | DOWN | 0.56 | 0.73 | 1.38 |
| 11-19 01:10 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-19 01:09 | +10 stop | ETH | UP | 0.59 | 0.74 | 1.19 |
| 11-19 01:09 | +10 stop | BNB | DOWN | 0.48 | 0.23 | -2.81 |
| 11-19 01:09 | +10 | BNB | DOWN | 0.50 | yes | -5.18 |
| 11-19 01:09 | +5 | BNB | DOWN | 0.51 | yes | -5.28 |
| 11-19 01:09 | +10 stop | XRP | DOWN | 0.55 | 0.26 | -3.22 |
| 11-19 01:08 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 11-19 01:08 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-19 01:08 | +10 stop | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-19 01:08 | +20 | BNB | UP | 0.47 | 0.74 | 2.38 |
| 11-19 01:08 | +15 | BNB | UP | 0.47 | 0.74 | 2.38 |
| 11-19 01:08 | +10 | BNB | UP | 0.47 | 0.59 | 0.85 |
| 11-19 01:08 | +5 | BNB | UP | 0.48 | 0.59 | 0.73 |
| 11-19 01:08 | +10 stop | XRP | UP | 0.44 | 0.63 | 1.55 |
| 11-19 01:08 | +10 stop | HYPE | UP | 0.42 | 0.53 | 0.74 |
| 11-19 01:08 | +10 stop | DOGE | UP | 0.46 | 0.67 | 1.76 |
| 11-19 01:08 | +10 stop | BTC | UP | 0.49 | 0.69 | 1.67 |
| 11-19 01:07 | +10 stop | NEAR | DOWN | 0.57 | 0.75 | 1.48 |
| 11-19 01:07 | +10 stop | ZEC | DOWN | 0.47 | 0.60 | 0.95 |
| 11-19 01:06 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 11-19 01:06 | +10 stop | BNB | UP | 0.63 | 0.84 | 1.84 |
| 11-19 01:06 | +10 | BNB | UP | 0.62 | 0.84 | 1.93 |
| 11-19 01:06 | +5 | BNB | UP | 0.62 | 0.68 | 0.27 |
| 11-19 01:06 | +10 stop | SOL | UP | 0.63 | 0.76 | 1.00 |
| 11-19 01:06 | +10 stop | BNB | UP | 0.56 | 0.67 | 0.76 |
| 11-19 01:06 | +15 | BNB | UP | 0.56 | 0.84 | 2.52 |
| 11-19 01:06 | +10 | BNB | UP | 0.56 | 0.67 | 0.76 |
| 11-19 01:06 | +5 | BNB | UP | 0.57 | 0.67 | 0.66 |
| 11-19 01:05 | +10 stop | DOGE | UP | 0.70 | 0.49 | -2.43 |
