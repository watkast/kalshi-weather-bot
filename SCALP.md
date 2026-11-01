# Range-Scalp Bot

*Updated Sun Nov 01 09:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43413 | 37832 | 5581 (63) | 2 | $-12390.57 | -4.5% |
| **+10¢** | 32385 | 25942 | 6443 (85) | 2 | $-11073.86 | -5.4% |
| **+15¢** | 27102 | 20163 | 6939 (112) | 2 | $-10108.42 | -5.9% |
| **+20¢** | 24069 | 16801 | 7268 (146) | 2 | $-8907.28 | -5.9% |
| **+10¢ (15¢ stop)** | 52940 | 52855 | 85 (50) | 2 | $-19985.26 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 09:15 | +10 stop | NEAR | UP | 0.53 | open |  |
| 11-01 09:15 | +20 | NEAR | UP | 0.53 | open |  |
| 11-01 09:15 | +15 | NEAR | UP | 0.53 | open |  |
| 11-01 09:15 | +10 | NEAR | UP | 0.53 | open |  |
| 11-01 09:15 | +5 | NEAR | UP | 0.53 | open |  |
| 11-01 09:15 | +10 stop | BTC | DOWN | 0.55 | open |  |
| 11-01 09:15 | +20 | BTC | DOWN | 0.55 | open |  |
| 11-01 09:15 | +15 | BTC | DOWN | 0.55 | open |  |
| 11-01 09:15 | +10 | BTC | DOWN | 0.55 | open |  |
| 11-01 09:15 | +5 | BTC | DOWN | 0.55 | open |  |
| 11-01 09:12 | +10 stop | XRP | DOWN | 0.53 | 0.72 | 1.57 |
| 11-01 09:08 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-01 09:07 | +10 stop | HYPE | DOWN | 0.51 | 0.81 | 2.70 |
| 11-01 09:05 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 11-01 09:05 | +10 stop | HYPE | DOWN | 0.52 | 0.66 | 1.06 |
| 11-01 09:05 | +10 stop | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-01 09:05 | +15 | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-01 09:05 | +10 | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-01 09:05 | +5 | NEAR | DOWN | 0.53 | 0.69 | 1.27 |
| 11-01 09:04 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 09:04 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-01 09:04 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-01 09:04 | +10 stop | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-01 09:04 | +10 | SOL | DOWN | 0.61 | 0.80 | 1.61 |
| 11-01 09:04 | +5 | SOL | DOWN | 0.61 | 0.69 | 0.48 |
| 11-01 09:04 | +10 stop | ZEC | DOWN | 0.62 | 0.41 | -2.44 |
| 11-01 09:03 | +10 stop | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 09:03 | +10 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 09:03 | +5 | BNB | DOWN | 0.59 | 0.71 | 0.88 |
| 11-01 09:03 | +10 stop | HYPE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-01 09:03 | +10 | HYPE | DOWN | 0.63 | 0.81 | 1.52 |
| 11-01 09:03 | +5 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-01 09:02 | +10 stop | XRP | UP | 0.61 | 0.73 | 0.89 |
| 11-01 09:02 | +10 stop | ZEC | UP | 0.61 | 0.41 | -2.34 |
| 11-01 09:02 | +20 | ZEC | UP | 0.61 | no | -6.27 |
| 11-01 09:02 | +15 | ZEC | UP | 0.61 | no | -6.27 |
| 11-01 09:02 | +10 | ZEC | UP | 0.61 | no | -6.27 |
| 11-01 09:02 | +5 | ZEC | UP | 0.61 | no | -6.27 |
| 11-01 09:02 | +10 stop | SOL | DOWN | 0.60 | 0.74 | 1.09 |
| 11-01 09:02 | +20 | SOL | DOWN | 0.60 | 0.80 | 1.71 |
