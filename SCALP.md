# Range-Scalp Bot

*Updated Fri Oct 09 09:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8840 | 7645 | 1195 (13) | 0 | $-2909.24 | -5.2% |
| **+10¢** | 6698 | 5294 | 1404 (25) | 0 | $-2802.53 | -6.6% |
| **+15¢** | 5650 | 4171 | 1479 (37) | 0 | $-2281.67 | -6.4% |
| **+20¢** | 5030 | 3495 | 1535 (45) | 0 | $-1878.25 | -5.9% |
| **+10¢ (15¢ stop)** | 10777 | 10747 | 30 (19) | 0 | $-4016.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 09:02 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-09 09:02 | +15 | ZEC | DOWN | 0.66 | 0.84 | 1.54 |
| 10-09 09:02 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-09 09:02 | +5 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-09 09:01 | +10 stop | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-09 09:01 | +20 | ZEC | DOWN | 0.48 | 0.69 | 1.77 |
| 10-09 09:01 | +15 | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-09 09:01 | +10 | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-09 09:01 | +5 | ZEC | DOWN | 0.48 | 0.63 | 1.15 |
| 10-09 08:58 | +5 | NEAR | UP | 0.70 | no | -7.15 |
| 10-09 08:57 | +10 stop | NEAR | UP | 0.57 | 0.37 | -2.32 |
| 10-09 08:57 | +20 | NEAR | UP | 0.57 | no | -5.85 |
| 10-09 08:57 | +15 | NEAR | UP | 0.57 | no | -5.85 |
| 10-09 08:57 | +10 | NEAR | UP | 0.57 | no | -5.85 |
| 10-09 08:57 | +5 | NEAR | UP | 0.57 | 0.65 | 0.49 |
| 10-09 08:54 | +10 stop | NEAR | DOWN | 0.56 | 0.33 | -2.64 |
| 10-09 08:52 | +10 stop | NEAR | DOWN | 0.69 | 0.50 | -2.22 |
| 10-09 08:51 | +10 stop | ZEC | UP | 0.67 | 0.84 | 1.44 |
| 10-09 08:51 | +10 stop | BNB | UP | 0.69 | 0.80 | 0.83 |
| 10-09 08:49 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-09 08:48 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 10-09 08:48 | +20 | HYPE | UP | 0.61 | 0.87 | 2.35 |
| 10-09 08:48 | +15 | HYPE | UP | 0.61 | 0.87 | 2.35 |
| 10-09 08:48 | +10 | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 10-09 08:48 | +5 | HYPE | UP | 0.65 | 0.72 | 0.39 |
| 10-09 08:47 | +5 | BNB | DOWN | 0.55 | yes | -5.67 |
| 10-09 08:47 | +10 stop | ZEC | DOWN | 0.63 | 0.43 | -2.35 |
| 10-09 08:47 | +20 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 10-09 08:47 | +15 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 10-09 08:47 | +10 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 10-09 08:47 | +5 | ZEC | DOWN | 0.63 | yes | -6.47 |
| 10-09 08:47 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-09 08:47 | +20 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-09 08:47 | +15 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-09 08:47 | +10 | ETH | UP | 0.61 | 0.74 | 0.99 |
| 10-09 08:47 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 10-09 08:46 | +10 stop | BNB | DOWN | 0.54 | 0.36 | -2.13 |
| 10-09 08:46 | +15 | BNB | DOWN | 0.54 | yes | -5.56 |
| 10-09 08:46 | +10 | BNB | DOWN | 0.54 | yes | -5.56 |
| 10-09 08:46 | +10 stop | XRP | UP | 0.59 | 0.72 | 0.98 |
