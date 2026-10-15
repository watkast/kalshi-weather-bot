# Range-Scalp Bot

*Updated Thu Oct 15 08:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17244 | 14975 | 2269 (28) | 1 | $-5221.04 | -4.8% |
| **+10¢** | 13033 | 10403 | 2630 (40) | 2 | $-4730.96 | -5.8% |
| **+15¢** | 10944 | 8117 | 2827 (59) | 2 | $-4215.14 | -6.1% |
| **+20¢** | 9725 | 6764 | 2961 (77) | 2 | $-3674.77 | -6.0% |
| **+10¢ (15¢ stop)** | 21187 | 21137 | 50 (29) | 0 | $-8179.38 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 06:57 | +10 stop | NEAR | DOWN | 0.54 | 0.33 | -2.44 |
| 10-15 06:57 | +15 | NEAR | DOWN | 0.54 | open |  |
| 10-15 06:57 | +10 | NEAR | DOWN | 0.55 | open |  |
| 10-15 06:57 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.16 |
| 10-15 06:55 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 06:53 | +10 stop | NEAR | DOWN | 0.48 | 0.60 | 0.85 |
| 10-15 06:48 | +10 stop | NEAR | DOWN | 0.66 | 0.50 | -1.94 |
| 10-15 06:48 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-15 06:48 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 06:48 | +10 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 06:48 | +5 | NEAR | DOWN | 0.66 | 0.72 | 0.29 |
| 10-15 06:48 | +10 stop | ZEC | DOWN | 0.48 | 0.29 | -2.22 |
| 10-15 06:48 | +20 | ZEC | DOWN | 0.48 | open |  |
| 10-15 06:48 | +15 | ZEC | DOWN | 0.48 | open |  |
| 10-15 06:48 | +10 | ZEC | DOWN | 0.48 | open |  |
| 10-15 06:48 | +5 | ZEC | DOWN | 0.48 | open |  |
| 10-15 06:47 | +10 stop | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 10-15 06:47 | +20 | HYPE | DOWN | 0.70 | 0.91 | 1.81 |
| 10-15 06:47 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.43 |
| 10-15 06:47 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.80 |
| 10-15 06:47 | +5 | HYPE | DOWN | 0.70 | 0.76 | 0.28 |
| 10-15 06:41 | +5 | ZEC | DOWN | 0.56 | 0.79 | 2.00 |
| 10-15 06:40 | +10 stop | ETH | DOWN | 0.57 | 0.23 | -3.71 |
| 10-15 06:40 | +10 stop | ZEC | UP | 0.40 | 0.20 | -2.29 |
| 10-15 06:40 | +10 | ZEC | UP | 0.40 | 0.50 | 0.65 |
| 10-15 06:40 | +5 | ZEC | UP | 0.40 | 0.46 | 0.25 |
| 10-15 06:39 | +10 stop | ZEC | UP | 0.50 | 0.62 | 0.85 |
| 10-15 06:39 | +15 | ZEC | UP | 0.50 | no | -5.18 |
| 10-15 06:39 | +10 | ZEC | UP | 0.50 | 0.62 | 0.85 |
| 10-15 06:39 | +5 | ZEC | UP | 0.50 | 0.62 | 0.85 |
| 10-15 06:38 | +10 stop | ETH | UP | 0.64 | 0.41 | -2.64 |
| 10-15 06:36 | +10 stop | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-15 06:36 | +10 | SOL | UP | 0.69 | 0.81 | 0.94 |
| 10-15 06:36 | +5 | SOL | UP | 0.69 | 0.74 | 0.21 |
| 10-15 06:36 | +10 stop | NEAR | UP | 0.61 | 0.72 | 0.78 |
| 10-15 06:35 | +10 stop | ETH | UP | 0.57 | 0.67 | 0.66 |
| 10-15 06:34 | +5 | BTC | UP | 0.69 | 0.78 | 0.62 |
| 10-15 06:34 | +10 stop | ETH | UP | 0.55 | 0.67 | 0.86 |
| 10-15 06:33 | +10 stop | NEAR | UP | 0.67 | 0.77 | 0.71 |
| 10-15 06:32 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
