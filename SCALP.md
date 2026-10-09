# Range-Scalp Bot

*Updated Fri Oct 09 20:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9429 | 8140 | 1289 (17) | 2 | $-3176.56 | -5.3% |
| **+10¢** | 7114 | 5601 | 1513 (29) | 4 | $-3115.06 | -7.0% |
| **+15¢** | 5994 | 4404 | 1590 (42) | 3 | $-2552.14 | -6.8% |
| **+20¢** | 5335 | 3683 | 1652 (53) | 5 | $-2136.90 | -6.4% |
| **+10¢ (15¢ stop)** | 11537 | 11505 | 32 (20) | 3 | $-4436.39 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 20:07 | +5 | ZEC | UP | 0.54 | 0.65 | 0.76 |
| 10-09 20:06 | +10 stop | ETH | DOWN | 0.63 | open |  |
| 10-09 20:06 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-09 20:06 | +10 stop | HYPE | DOWN | 0.59 | open |  |
| 10-09 20:06 | +10 | HYPE | DOWN | 0.59 | open |  |
| 10-09 20:06 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.36 |
| 10-09 20:06 | +10 stop | ZEC | UP | 0.62 | 0.47 | -1.88 |
| 10-09 20:06 | +20 | ZEC | UP | 0.62 | open |  |
| 10-09 20:06 | +15 | ZEC | UP | 0.62 | open |  |
| 10-09 20:06 | +5 | ZEC | UP | 0.61 | 0.67 | 0.29 |
| 10-09 20:06 | +10 stop | BTC | UP | 0.61 | open |  |
| 10-09 20:05 | +5 | ETH | DOWN | 0.56 | 0.68 | 0.86 |
| 10-09 20:05 | +10 stop | HYPE | DOWN | 0.50 | 0.61 | 0.75 |
| 10-09 20:05 | +20 | HYPE | DOWN | 0.50 | open |  |
| 10-09 20:05 | +15 | HYPE | DOWN | 0.50 | 0.65 | 1.16 |
| 10-09 20:05 | +10 | HYPE | DOWN | 0.50 | 0.61 | 0.75 |
| 10-09 20:05 | +5 | HYPE | DOWN | 0.50 | 0.55 | 0.14 |
| 10-09 20:04 | +10 stop | ETH | DOWN | 0.58 | 0.68 | 0.66 |
| 10-09 20:04 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-09 20:04 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-09 20:04 | +20 | NEAR | UP | 0.70 | open |  |
| 10-09 20:04 | +15 | NEAR | UP | 0.70 | 0.85 | 1.26 |
| 10-09 20:04 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-09 20:04 | +5 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-09 20:04 | +5 | BTC | UP | 0.53 | open |  |
| 10-09 20:02 | +10 | ZEC | UP | 0.70 | open |  |
| 10-09 20:01 | +10 stop | ETH | UP | 0.70 | 0.48 | -2.53 |
| 10-09 20:01 | +20 | ETH | UP | 0.70 | open |  |
| 10-09 20:01 | +15 | ETH | UP | 0.70 | open |  |
| 10-09 20:01 | +10 | ETH | UP | 0.70 | open |  |
| 10-09 20:01 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 10-09 20:01 | +10 stop | BTC | UP | 0.71 | 0.49 | -2.53 |
| 10-09 20:01 | +20 | BTC | UP | 0.71 | open |  |
| 10-09 20:01 | +15 | BTC | UP | 0.71 | open |  |
| 10-09 20:01 | +10 | BTC | UP | 0.71 | open |  |
| 10-09 20:01 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 10-09 19:55 | +10 stop | NEAR | UP | 0.48 | 0.31 | -2.00 |
| 10-09 19:55 | +10 | NEAR | UP | 0.48 | no | -4.95 |
| 10-09 19:55 | +5 | NEAR | UP | 0.48 | no | -4.95 |
| 10-09 19:55 | +5 | DOGE | UP | 0.41 | 0.57 | 1.25 |
