# Range-Scalp Bot

*Updated Wed Nov 18 16:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64208 | 55993 | 8215 (124) | 0 | $-17578.18 | -4.3% |
| **+10¢** | 47953 | 38340 | 9613 (165) | 0 | $-16480.79 | -5.5% |
| **+15¢** | 40203 | 29842 | 10361 (210) | 0 | $-14933.42 | -5.9% |
| **+20¢** | 35799 | 24924 | 10875 (265) | 0 | $-13238.91 | -5.9% |
| **+10¢ (15¢ stop)** | 78107 | 77943 | 164 (98) | 0 | $-28740.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 16:17 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-18 16:17 | +20 | XRP | DOWN | 0.69 | 0.93 | 2.16 |
| 11-18 16:17 | +15 | XRP | DOWN | 0.69 | 0.93 | 2.16 |
| 11-18 16:17 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-18 16:17 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-18 16:16 | +10 stop | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-18 16:16 | +20 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-18 16:16 | +15 | BTC | DOWN | 0.64 | 0.84 | 1.73 |
| 11-18 16:16 | +10 | BTC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-18 16:16 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-18 16:16 | +10 stop | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-18 16:16 | +20 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-18 16:16 | +15 | ZEC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-18 16:16 | +10 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-18 16:16 | +5 | ZEC | DOWN | 0.65 | 0.77 | 0.91 |
| 11-18 16:15 | +10 stop | HYPE | DOWN | 0.63 | 0.74 | 0.80 |
| 11-18 16:15 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-18 16:15 | +15 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-18 16:15 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-18 16:15 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.38 |
| 11-18 16:15 | +10 stop | DOGE | DOWN | 0.56 | 0.75 | 1.58 |
| 11-18 16:15 | +20 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 11-18 16:15 | +15 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 11-18 16:15 | +10 | DOGE | DOWN | 0.55 | 0.75 | 1.68 |
| 11-18 16:15 | +5 | DOGE | DOWN | 0.57 | 0.75 | 1.48 |
| 11-18 16:11 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 11-18 16:10 | +5 | NEAR | UP | 0.65 | no | -6.66 |
| 11-18 16:10 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 11-18 16:09 | +10 stop | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +15 | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +10 | XRP | DOWN | 0.49 | 0.70 | 1.77 |
| 11-18 16:09 | +5 | XRP | DOWN | 0.49 | 0.55 | 0.24 |
| 11-18 16:09 | +10 stop | DOGE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-18 16:09 | +10 stop | ZEC | DOWN | 0.68 | 0.24 | -4.69 |
| 11-18 16:09 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-18 16:09 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 16:09 | +5 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-18 16:09 | +10 stop | NEAR | UP | 0.53 | 0.32 | -2.48 |
| 11-18 16:09 | +10 | NEAR | UP | 0.53 | no | -5.52 |
| 11-18 16:09 | +5 | NEAR | UP | 0.53 | 0.61 | 0.41 |
