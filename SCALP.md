# Range-Scalp Bot

*Updated Fri Nov 06 07:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49409 | 43054 | 6355 (75) | 4 | $-14008.14 | -4.5% |
| **+10¢** | 36886 | 29497 | 7389 (101) | 5 | $-12881.43 | -5.6% |
| **+15¢** | 30898 | 22942 | 7956 (130) | 5 | $-11758.25 | -6.1% |
| **+20¢** | 27466 | 19128 | 8338 (170) | 5 | $-10393.74 | -6.0% |
| **+10¢ (15¢ stop)** | 60242 | 60147 | 95 (57) | 1 | $-22329.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 07:57 | +10 stop | SOL | UP | 0.71 | open |  |
| 11-06 07:55 | +10 stop | SOL | UP | 0.64 | 0.46 | -2.15 |
| 11-06 07:54 | +10 stop | XRP | UP | 0.67 | 0.78 | 0.81 |
| 11-06 07:54 | +5 | XRP | UP | 0.67 | 0.78 | 0.81 |
| 11-06 07:54 | +10 stop | BNB | UP | 0.66 | 0.79 | 1.02 |
| 11-06 07:53 | +15 | XRP | DOWN | 0.53 | open |  |
| 11-06 07:53 | +10 | XRP | DOWN | 0.53 | open |  |
| 11-06 07:53 | +5 | XRP | DOWN | 0.53 | 0.58 | 0.14 |
| 11-06 07:52 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 11-06 07:52 | +10 stop | BNB | UP | 0.66 | 0.50 | -1.89 |
| 11-06 07:52 | +15 | BNB | UP | 0.66 | 0.87 | 1.91 |
| 11-06 07:52 | +10 | BNB | UP | 0.66 | 0.79 | 1.07 |
| 11-06 07:52 | +5 | BNB | UP | 0.66 | 0.71 | 0.24 |
| 11-06 07:51 | +10 stop | NEAR | DOWN | 0.61 | 0.40 | -2.44 |
| 11-06 07:51 | +10 stop | SOL | DOWN | 0.71 | 0.56 | -1.83 |
| 11-06 07:51 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-06 07:51 | +10 stop | XRP | DOWN | 0.64 | 0.41 | -2.64 |
| 11-06 07:51 | +10 stop | DOGE | UP | 0.65 | 0.78 | 1.01 |
| 11-06 07:51 | +10 stop | HYPE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-06 07:51 | +5 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-06 07:50 | +10 stop | HYPE | UP | 0.56 | 0.41 | -1.85 |
| 11-06 07:50 | +10 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-06 07:50 | +5 | HYPE | UP | 0.56 | 0.66 | 0.66 |
| 11-06 07:50 | +10 stop | ZEC | UP | 0.55 | 0.36 | -2.25 |
| 11-06 07:50 | +10 stop | SOL | UP | 0.67 | 0.51 | -1.94 |
| 11-06 07:50 | +5 | SOL | UP | 0.67 | open |  |
| 11-06 07:49 | +10 stop | XRP | UP | 0.71 | 0.53 | -2.13 |
| 11-06 07:49 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 11-06 07:49 | +10 stop | NEAR | UP | 0.66 | 0.44 | -2.54 |
| 11-06 07:49 | +10 stop | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 11-06 07:49 | +10 stop | ZEC | DOWN | 0.63 | 0.42 | -2.45 |
| 11-06 07:48 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 11-06 07:48 | +20 | HYPE | UP | 0.57 | 0.81 | 2.11 |
| 11-06 07:48 | +15 | HYPE | UP | 0.57 | 0.81 | 2.11 |
| 11-06 07:48 | +10 | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 11-06 07:48 | +5 | HYPE | UP | 0.58 | 0.69 | 0.77 |
| 11-06 07:48 | +10 stop | SOL | UP | 0.48 | 0.69 | 1.77 |
| 11-06 07:47 | +10 stop | XRP | UP | 0.67 | 0.52 | -1.84 |
| 11-06 07:47 | +10 stop | DOGE | UP | 0.60 | 0.70 | 0.68 |
| 11-06 07:47 | +10 stop | BNB | UP | 0.65 | 0.75 | 0.70 |
