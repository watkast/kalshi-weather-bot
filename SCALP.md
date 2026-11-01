# Range-Scalp Bot

*Updated Sun Nov 01 00:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42953 | 37447 | 5506 (62) | 4 | $-12157.91 | -4.5% |
| **+10¢** | 32030 | 25665 | 6365 (84) | 4 | $-10902.05 | -5.4% |
| **+15¢** | 26796 | 19933 | 6863 (112) | 3 | $-9989.16 | -5.9% |
| **+20¢** | 23802 | 16611 | 7191 (145) | 3 | $-8833.06 | -5.9% |
| **+10¢ (15¢ stop)** | 52393 | 52310 | 83 (48) | 3 | $-19858.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 00:31 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-01 00:31 | +20 | ZEC | UP | 0.65 | open |  |
| 11-01 00:31 | +15 | ZEC | UP | 0.65 | open |  |
| 11-01 00:31 | +10 | ZEC | UP | 0.65 | open |  |
| 11-01 00:31 | +5 | ZEC | UP | 0.65 | open |  |
| 11-01 00:31 | +10 stop | HYPE | UP | 0.67 | open |  |
| 11-01 00:31 | +20 | HYPE | UP | 0.67 | open |  |
| 11-01 00:31 | +15 | HYPE | UP | 0.67 | open |  |
| 11-01 00:31 | +10 | HYPE | UP | 0.67 | open |  |
| 11-01 00:31 | +5 | HYPE | UP | 0.67 | open |  |
| 11-01 00:31 | +10 | DOGE | UP | 0.71 | open |  |
| 11-01 00:31 | +5 | DOGE | UP | 0.71 | open |  |
| 11-01 00:31 | +10 stop | ETH | UP | 0.66 | open |  |
| 11-01 00:31 | +20 | ETH | UP | 0.66 | open |  |
| 11-01 00:31 | +15 | ETH | UP | 0.66 | open |  |
| 11-01 00:31 | +10 | ETH | UP | 0.66 | open |  |
| 11-01 00:31 | +5 | ETH | UP | 0.66 | open |  |
| 11-01 00:25 | +10 stop | XRP | UP | 0.56 | 0.90 | 3.15 |
| 11-01 00:24 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-01 00:24 | +10 stop | DOGE | UP | 0.64 | 0.81 | 1.42 |
| 11-01 00:24 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 11-01 00:24 | +10 stop | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-01 00:24 | +5 | DOGE | UP | 0.55 | 0.81 | 2.31 |
| 11-01 00:23 | +10 stop | DOGE | DOWN | 0.54 | 0.38 | -1.95 |
| 11-01 00:23 | +20 | DOGE | DOWN | 0.54 | yes | -5.58 |
| 11-01 00:23 | +15 | DOGE | DOWN | 0.54 | yes | -5.58 |
| 11-01 00:23 | +10 | DOGE | DOWN | 0.54 | yes | -5.58 |
| 11-01 00:23 | +5 | DOGE | DOWN | 0.54 | 0.63 | 0.55 |
| 11-01 00:23 | +10 stop | NEAR | UP | 0.69 | 0.95 | 2.38 |
| 11-01 00:23 | +10 stop | XRP | DOWN | 0.57 | 0.35 | -2.59 |
| 11-01 00:23 | +10 | XRP | DOWN | 0.57 | yes | -5.88 |
| 11-01 00:23 | +5 | XRP | DOWN | 0.57 | yes | -5.93 |
| 11-01 00:23 | +10 stop | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 00:23 | +20 | XRP | DOWN | 0.57 | yes | -5.88 |
| 11-01 00:23 | +15 | XRP | DOWN | 0.57 | yes | -5.88 |
| 11-01 00:23 | +10 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 00:23 | +5 | XRP | DOWN | 0.57 | 0.67 | 0.66 |
| 11-01 00:22 | +5 | ETH | DOWN | 0.63 | yes | -6.47 |
| 11-01 00:22 | +10 stop | SOL | DOWN | 0.52 | 0.28 | -2.73 |
| 11-01 00:22 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
