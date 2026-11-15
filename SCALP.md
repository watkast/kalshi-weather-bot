# Range-Scalp Bot

*Updated Sun Nov 15 22:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61350 | 53533 | 7817 (114) | 3 | $-16522.06 | -4.3% |
| **+10¢** | 45812 | 36653 | 9159 (153) | 6 | $-15521.12 | -5.4% |
| **+15¢** | 38373 | 28494 | 9879 (191) | 7 | $-14173.39 | -5.9% |
| **+20¢** | 34202 | 23840 | 10362 (243) | 8 | $-12438.73 | -5.8% |
| **+10¢ (15¢ stop)** | 74662 | 74510 | 152 (90) | 2 | $-27463.42 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 22:57 | +5 | DOGE | DOWN | 0.63 | 0.71 | 0.48 |
| 11-15 22:57 | +10 stop | NEAR | DOWN | 0.70 | open |  |
| 11-15 22:57 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-15 22:57 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-15 22:57 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-15 22:57 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 11-15 22:56 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-15 22:56 | +10 stop | BTC | DOWN | 0.65 | 0.47 | -2.14 |
| 11-15 22:56 | +10 stop | BNB | UP | 0.62 | 0.72 | 0.68 |
| 11-15 22:56 | +20 | BNB | UP | 0.63 | open |  |
| 11-15 22:55 | +10 stop | XRP | DOWN | 0.56 | 0.74 | 1.45 |
| 11-15 22:55 | +20 | XRP | DOWN | 0.55 | open |  |
| 11-15 22:55 | +15 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 11-15 22:55 | +10 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 11-15 22:55 | +5 | XRP | DOWN | 0.55 | 0.74 | 1.58 |
| 11-15 22:54 | +10 stop | DOGE | UP | 0.64 | 0.36 | -3.14 |
| 11-15 22:54 | +10 stop | BTC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-15 22:53 | +10 stop | DOGE | DOWN | 0.60 | 0.34 | -2.93 |
| 11-15 22:53 | +10 stop | SOL | DOWN | 0.53 | 0.35 | -2.14 |
| 11-15 22:53 | +5 | DOGE | DOWN | 0.60 | 0.69 | 0.58 |
| 11-15 22:53 | +10 stop | HYPE | UP | 0.60 | 0.72 | 0.90 |
| 11-15 22:52 | +10 stop | SOL | UP | 0.65 | 0.45 | -2.34 |
| 11-15 22:51 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-15 22:51 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-15 22:50 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-15 22:50 | +10 stop | SOL | DOWN | 0.53 | 0.36 | -2.05 |
| 11-15 22:50 | +10 stop | HYPE | DOWN | 0.70 | 0.48 | -2.53 |
| 11-15 22:49 | +10 stop | BNB | UP | 0.57 | 0.73 | 1.28 |
| 11-15 22:49 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 11-15 22:49 | +10 stop | XRP | DOWN | 0.71 | 0.55 | -1.93 |
| 11-15 22:49 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 11-15 22:49 | +10 | DOGE | UP | 0.58 | open |  |
| 11-15 22:49 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-15 22:49 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-15 22:49 | +10 stop | BTC | UP | 0.62 | 0.44 | -2.15 |
| 11-15 22:49 | +15 | BTC | UP | 0.62 | open |  |
| 11-15 22:49 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 11-15 22:49 | +5 | BTC | UP | 0.62 | 0.68 | 0.27 |
| 11-15 22:49 | +10 stop | ZEC | UP | 0.58 | 0.30 | -3.13 |
| 11-15 22:49 | +15 | ZEC | UP | 0.58 | open |  |
