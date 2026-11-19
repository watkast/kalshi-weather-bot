# Range-Scalp Bot

*Updated Thu Nov 19 07:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64917 | 56654 | 8263 (124) | 0 | $-17483.35 | -4.3% |
| **+10¢** | 48491 | 38825 | 9666 (165) | 0 | $-16267.54 | -5.3% |
| **+15¢** | 40667 | 30243 | 10424 (210) | 0 | $-14670.42 | -5.7% |
| **+20¢** | 36215 | 25269 | 10946 (265) | 0 | $-12962.94 | -5.7% |
| **+10¢ (15¢ stop)** | 78989 | 78825 | 164 (98) | 0 | $-29001.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 06:58 | +10 stop | NEAR | UP | 0.68 | 0.96 | 2.65 |
| 11-19 06:58 | +10 | NEAR | UP | 0.68 | 0.96 | 2.65 |
| 11-19 06:57 | +10 stop | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-19 06:57 | +10 stop | NEAR | UP | 0.47 | 0.59 | 0.88 |
| 11-19 06:56 | +10 stop | ZEC | DOWN | 0.52 | 0.64 | 0.85 |
| 11-19 06:56 | +10 stop | ETH | UP | 0.71 | 0.92 | 1.86 |
| 11-19 06:56 | +20 | ETH | UP | 0.70 | 0.92 | 1.96 |
| 11-19 06:56 | +15 | ETH | UP | 0.70 | 0.92 | 1.96 |
| 11-19 06:56 | +10 | ETH | UP | 0.70 | 0.92 | 1.96 |
| 11-19 06:56 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-19 06:56 | +10 stop | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 11-19 06:56 | +20 | DOGE | UP | 0.67 | 0.88 | 1.86 |
| 11-19 06:56 | +15 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 11-19 06:56 | +10 | DOGE | UP | 0.67 | 0.85 | 1.55 |
| 11-19 06:56 | +5 | DOGE | UP | 0.67 | 0.72 | 0.19 |
| 11-19 06:55 | +5 | NEAR | UP | 0.70 | 0.96 | 2.46 |
| 11-19 06:54 | +5 | NEAR | UP | 0.59 | 0.65 | 0.27 |
| 11-19 06:54 | +5 | ZEC | UP | 0.63 | no | -6.47 |
| 11-19 06:54 | +10 stop | NEAR | UP | 0.59 | 0.72 | 0.98 |
| 11-19 06:53 | +5 | ZEC | UP | 0.51 | 0.61 | 0.65 |
| 11-19 06:53 | +10 stop | BNB | UP | 0.65 | 0.83 | 1.54 |
| 11-19 06:53 | +10 stop | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 11-19 06:53 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 11-19 06:53 | +5 | ZEC | UP | 0.62 | 0.67 | 0.17 |
| 11-19 06:53 | +10 stop | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 11-19 06:53 | +5 | HYPE | UP | 0.59 | 0.70 | 0.78 |
| 11-19 06:52 | +10 stop | NEAR | DOWN | 0.64 | 0.49 | -1.85 |
| 11-19 06:52 | +10 stop | BNB | DOWN | 0.56 | 0.38 | -2.15 |
| 11-19 06:51 | +10 stop | ETH | UP | 0.56 | 0.71 | 1.17 |
| 11-19 06:51 | +10 stop | BTC | DOWN | 0.57 | 0.36 | -2.45 |
| 11-19 06:51 | +10 stop | BNB | DOWN | 0.49 | 0.60 | 0.75 |
| 11-19 06:51 | +10 stop | ZEC | DOWN | 0.48 | 0.32 | -1.94 |
| 11-19 06:51 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-19 06:51 | +10 stop | DOGE | DOWN | 0.55 | 0.34 | -2.44 |
| 11-19 06:50 | +10 stop | ETH | DOWN | 0.60 | 0.45 | -1.85 |
| 11-19 06:50 | +10 stop | DOGE | DOWN | 0.56 | 0.69 | 0.97 |
| 11-19 06:49 | +10 stop | HYPE | DOWN | 0.64 | 0.41 | -2.63 |
| 11-19 06:49 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-19 06:49 | +15 | XRP | UP | 0.63 | 0.82 | 1.62 |
| 11-19 06:49 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
