# Range-Scalp Bot

*Updated Sun Oct 18 09:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 22348 | 19454 | 2894 (29) | 5 | $-6509.73 | -4.6% |
| **+10¢** | 16823 | 13478 | 3345 (43) | 7 | $-5800.94 | -5.5% |
| **+15¢** | 14087 | 10478 | 3609 (63) | 8 | $-5307.06 | -6.0% |
| **+20¢** | 12464 | 8684 | 3780 (81) | 9 | $-4756.18 | -6.1% |
| **+10¢ (15¢ stop)** | 27499 | 27449 | 50 (29) | 4 | $-10524.04 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-18 09:20 | +5 | DOGE | DOWN | 0.71 | open |  |
| 10-18 09:20 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 10-18 09:19 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-18 09:19 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 10-18 09:19 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.30 |
| 10-18 09:19 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-18 09:18 | +10 | DOGE | DOWN | 0.61 | open |  |
| 10-18 09:18 | +5 | DOGE | DOWN | 0.61 | 0.69 | 0.50 |
| 10-18 09:18 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 10-18 09:18 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-18 09:18 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 09:18 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-18 09:18 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-18 09:18 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 10-18 09:18 | +20 | BNB | DOWN | 0.62 | open |  |
| 10-18 09:18 | +15 | BNB | DOWN | 0.62 | open |  |
| 10-18 09:18 | +10 | BNB | DOWN | 0.62 | open |  |
| 10-18 09:18 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.45 |
| 10-18 09:17 | +5 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-18 09:17 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.23 |
| 10-18 09:16 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-18 09:16 | +20 | HYPE | DOWN | 0.62 | open |  |
| 10-18 09:16 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-18 09:16 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-18 09:16 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-18 09:16 | +5 | DOGE | UP | 0.56 | 0.62 | 0.25 |
| 10-18 09:16 | +10 stop | SOL | UP | 0.55 | 0.39 | -1.95 |
| 10-18 09:16 | +20 | SOL | UP | 0.55 | open |  |
| 10-18 09:16 | +15 | SOL | UP | 0.55 | open |  |
| 10-18 09:16 | +10 | SOL | UP | 0.55 | open |  |
| 10-18 09:16 | +5 | SOL | UP | 0.55 | open |  |
| 10-18 09:16 | +10 stop | DOGE | UP | 0.53 | 0.35 | -2.14 |
| 10-18 09:16 | +20 | DOGE | UP | 0.52 | open |  |
| 10-18 09:16 | +15 | DOGE | UP | 0.52 | open |  |
| 10-18 09:16 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 10-18 09:16 | +5 | DOGE | UP | 0.52 | 0.57 | 0.14 |
| 10-18 09:16 | +10 stop | XRP | UP | 0.46 | 0.30 | -1.93 |
| 10-18 09:16 | +20 | XRP | UP | 0.46 | open |  |
| 10-18 09:16 | +15 | XRP | UP | 0.46 | open |  |
| 10-18 09:16 | +10 | XRP | UP | 0.46 | open |  |
