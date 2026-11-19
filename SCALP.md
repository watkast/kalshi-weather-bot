# Range-Scalp Bot

*Updated Thu Nov 19 05:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64854 | 56597 | 8257 (124) | 1 | $-17479.22 | -4.3% |
| **+10¢** | 48447 | 38789 | 9658 (165) | 1 | $-16264.05 | -5.3% |
| **+15¢** | 40628 | 30212 | 10416 (210) | 0 | $-14676.88 | -5.8% |
| **+20¢** | 36178 | 25240 | 10938 (265) | 0 | $-12982.69 | -5.7% |
| **+10¢ (15¢ stop)** | 78906 | 78742 | 164 (98) | 0 | $-28973.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 05:57 | +10 stop | ETH | UP | 0.65 | 0.47 | -2.14 |
| 11-19 05:56 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-19 05:56 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-19 05:55 | +10 stop | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 11-19 05:55 | +5 | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 11-19 05:55 | +10 stop | NEAR | UP | 0.65 | 0.81 | 1.36 |
| 11-19 05:55 | +10 | NEAR | UP | 0.65 | 0.81 | 1.32 |
| 11-19 05:55 | +5 | NEAR | UP | 0.65 | 0.81 | 1.32 |
| 11-19 05:54 | +10 stop | ETH | UP | 0.54 | 0.66 | 0.86 |
| 11-19 05:53 | +10 stop | ZEC | UP | 0.62 | 0.84 | 1.93 |
| 11-19 05:53 | +5 | ZEC | UP | 0.62 | 0.84 | 1.93 |
| 11-19 05:53 | +15 | DOGE | UP | 0.66 | 0.82 | 1.37 |
| 11-19 05:53 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 11-19 05:53 | +10 stop | BNB | DOWN | 0.62 | 0.23 | -4.20 |
| 11-19 05:53 | +10 stop | BTC | DOWN | 0.57 | 0.28 | -3.23 |
| 11-19 05:52 | +10 stop | ZEC | DOWN | 0.62 | 0.37 | -2.84 |
| 11-19 05:52 | +20 | XRP | UP | 0.66 | 0.87 | 1.91 |
| 11-19 05:52 | +15 | XRP | UP | 0.66 | 0.87 | 1.91 |
| 11-19 05:52 | +10 | XRP | UP | 0.66 | 0.80 | 1.17 |
| 11-19 05:52 | +10 stop | SOL | DOWN | 0.57 | 0.32 | -2.84 |
| 11-19 05:51 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-19 05:51 | +5 | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-19 05:51 | +10 stop | NEAR | UP | 0.64 | 0.79 | 1.21 |
| 11-19 05:51 | +10 stop | HYPE | UP | 0.56 | 0.73 | 1.38 |
| 11-19 05:51 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
| 11-19 05:51 | +10 stop | DOGE | DOWN | 0.53 | 0.38 | -1.85 |
| 11-19 05:51 | +10 | DOGE | DOWN | 0.53 | open |  |
| 11-19 05:51 | +5 | DOGE | DOWN | 0.53 | open |  |
| 11-19 05:51 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-19 05:51 | +5 | HYPE | UP | 0.67 | 0.73 | 0.30 |
| 11-19 05:51 | +10 stop | SOL | DOWN | 0.46 | 0.60 | 1.05 |
| 11-19 05:51 | +10 stop | BTC | DOWN | 0.54 | 0.71 | 1.37 |
| 11-19 05:50 | +10 stop | ZEC | UP | 0.56 | 0.39 | -2.05 |
| 11-19 05:50 | +20 | ZEC | UP | 0.56 | 0.84 | 2.52 |
| 11-19 05:50 | +15 | ZEC | UP | 0.56 | 0.84 | 2.52 |
| 11-19 05:50 | +10 | ZEC | UP | 0.56 | 0.84 | 2.52 |
| 11-19 05:50 | +5 | ZEC | UP | 0.56 | 0.62 | 0.25 |
| 11-19 05:49 | +10 stop | SOL | UP | 0.53 | 0.35 | -2.14 |
| 11-19 05:49 | +15 | SOL | UP | 0.53 | 0.73 | 1.68 |
| 11-19 05:49 | +10 | SOL | UP | 0.56 | 0.67 | 0.76 |
