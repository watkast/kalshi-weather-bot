# Range-Scalp Bot

*Updated Wed Nov 18 16:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64224 | 56009 | 8215 (124) | 2 | $-17570.23 | -4.3% |
| **+10¢** | 47966 | 38353 | 9613 (165) | 3 | $-16465.80 | -5.5% |
| **+15¢** | 40214 | 29853 | 10361 (210) | 3 | $-14911.86 | -5.9% |
| **+20¢** | 35809 | 24934 | 10875 (265) | 3 | $-13216.07 | -5.9% |
| **+10¢ (15¢ stop)** | 78137 | 77973 | 164 (98) | 0 | $-28765.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 16:42 | +10 stop | NEAR | DOWN | 0.67 | 0.52 | -1.84 |
| 11-18 16:42 | +5 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 16:40 | +10 stop | HYPE | DOWN | 0.54 | 0.36 | -2.15 |
| 11-18 16:39 | +10 stop | HYPE | UP | 0.53 | 0.34 | -2.24 |
| 11-18 16:39 | +10 stop | NEAR | UP | 0.58 | 0.33 | -2.84 |
| 11-18 16:39 | +10 | NEAR | UP | 0.58 | open |  |
| 11-18 16:39 | +5 | NEAR | UP | 0.58 | 0.65 | 0.36 |
| 11-18 16:38 | +10 stop | HYPE | UP | 0.69 | 0.54 | -1.83 |
| 11-18 16:38 | +20 | HYPE | UP | 0.69 | 0.90 | 1.90 |
| 11-18 16:38 | +15 | HYPE | UP | 0.69 | 0.87 | 1.57 |
| 11-18 16:38 | +10 | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 11-18 16:38 | +5 | HYPE | UP | 0.69 | 0.81 | 0.94 |
| 11-18 16:37 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-18 16:37 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-18 16:37 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-18 16:37 | +15 | XRP | UP | 0.53 | open |  |
| 11-18 16:36 | +10 stop | XRP | UP | 0.61 | 0.41 | -2.34 |
| 11-18 16:36 | +10 | XRP | UP | 0.62 | open |  |
| 11-18 16:36 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 11-18 16:36 | +5 | XRP | UP | 0.69 | open |  |
| 11-18 16:36 | +10 stop | ZEC | DOWN | 0.48 | 0.59 | 0.75 |
| 11-18 16:35 | +10 stop | ZEC | DOWN | 0.48 | 0.64 | 1.25 |
| 11-18 16:35 | +10 stop | BTC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-18 16:35 | +10 stop | BNB | DOWN | 0.61 | 0.41 | -2.34 |
| 11-18 16:34 | +10 stop | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 11-18 16:34 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-18 16:34 | +20 | NEAR | UP | 0.70 | open |  |
| 11-18 16:34 | +15 | NEAR | UP | 0.71 | open |  |
| 11-18 16:34 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 11-18 16:34 | +10 stop | ZEC | UP | 0.54 | 0.37 | -2.05 |
| 11-18 16:34 | +10 stop | XRP | UP | 0.53 | 0.63 | 0.65 |
| 11-18 16:34 | +20 | XRP | UP | 0.52 | open |  |
| 11-18 16:34 | +15 | XRP | UP | 0.52 | 0.68 | 1.26 |
| 11-18 16:34 | +10 | XRP | UP | 0.52 | 0.63 | 0.75 |
| 11-18 16:34 | +5 | XRP | UP | 0.53 | 0.58 | 0.14 |
| 11-18 16:33 | +10 stop | DOGE | UP | 0.66 | 0.38 | -3.13 |
| 11-18 16:33 | +20 | DOGE | UP | 0.66 | open |  |
| 11-18 16:33 | +15 | DOGE | UP | 0.66 | open |  |
| 11-18 16:33 | +10 | DOGE | UP | 0.66 | open |  |
| 11-18 16:33 | +5 | DOGE | UP | 0.66 | open |  |
