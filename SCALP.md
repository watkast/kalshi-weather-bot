# Range-Scalp Bot

*Updated Wed Oct 21 16:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27417 | 23871 | 3546 (39) | 0 | $-8005.32 | -4.6% |
| **+10¢** | 20614 | 16518 | 4096 (55) | 3 | $-7077.62 | -5.5% |
| **+15¢** | 17263 | 12856 | 4407 (78) | 5 | $-6324.40 | -5.8% |
| **+20¢** | 15281 | 10663 | 4618 (98) | 5 | $-5680.45 | -5.9% |
| **+10¢ (15¢ stop)** | 33636 | 33577 | 59 (32) | 0 | $-12515.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 16:09 | +10 stop | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-21 16:09 | +20 | DOGE | DOWN | 0.66 | 0.96 | 2.81 |
| 10-21 16:09 | +15 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-21 16:09 | +10 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-21 16:09 | +5 | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-21 16:09 | +10 stop | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-21 16:09 | +10 | XRP | DOWN | 0.65 | 0.86 | 1.85 |
| 10-21 16:09 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 10-21 16:09 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-21 16:08 | +15 | XRP | UP | 0.47 | open |  |
| 10-21 16:08 | +10 | XRP | UP | 0.47 | 0.60 | 0.95 |
| 10-21 16:08 | +5 | XRP | UP | 0.47 | 0.60 | 0.95 |
| 10-21 16:08 | +10 stop | XRP | UP | 0.50 | 0.60 | 0.65 |
| 10-21 16:08 | +5 | BNB | UP | 0.63 | 0.69 | 0.28 |
| 10-21 16:08 | +10 stop | SOL | UP | 0.62 | 0.36 | -2.94 |
| 10-21 16:08 | +10 stop | HYPE | DOWN | 0.59 | 0.35 | -2.73 |
| 10-21 16:08 | +20 | HYPE | DOWN | 0.59 | open |  |
| 10-21 16:08 | +15 | HYPE | DOWN | 0.59 | open |  |
| 10-21 16:08 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-21 16:08 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-21 16:08 | +5 | ETH | DOWN | 0.44 | 0.72 | 2.47 |
| 10-21 16:08 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-21 16:08 | +5 | BNB | UP | 0.59 | 0.67 | 0.47 |
| 10-21 16:07 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-21 16:07 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-21 16:07 | +10 stop | ETH | DOWN | 0.49 | 0.30 | -2.23 |
| 10-21 16:07 | +10 | ETH | DOWN | 0.49 | 0.72 | 1.97 |
| 10-21 16:07 | +5 | ETH | DOWN | 0.49 | 0.57 | 0.44 |
| 10-21 16:07 | +10 stop | SOL | DOWN | 0.58 | 0.41 | -2.05 |
| 10-21 16:07 | +15 | SOL | DOWN | 0.58 | 0.81 | 2.01 |
| 10-21 16:07 | +10 | SOL | DOWN | 0.58 | 0.81 | 2.01 |
| 10-21 16:07 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-21 16:05 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 10-21 16:05 | +5 | SOL | DOWN | 0.56 | 0.63 | 0.35 |
| 10-21 16:05 | +10 stop | BTC | UP | 0.48 | 0.64 | 1.25 |
| 10-21 16:04 | +5 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-21 16:03 | +5 | ZEC | DOWN | 0.52 | 0.71 | 1.57 |
| 10-21 16:03 | +10 stop | HYPE | DOWN | 0.57 | 0.75 | 1.44 |
| 10-21 16:03 | +20 | HYPE | DOWN | 0.57 | 0.78 | 1.79 |
| 10-21 16:03 | +15 | HYPE | DOWN | 0.57 | 0.75 | 1.48 |
