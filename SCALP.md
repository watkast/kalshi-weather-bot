# Range-Scalp Bot

*Updated Thu Nov 05 06:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48171 | 41958 | 6213 (73) | 4 | $-13823.13 | -4.6% |
| **+10¢** | 35970 | 28753 | 7217 (99) | 5 | $-12681.59 | -5.6% |
| **+15¢** | 30144 | 22374 | 7770 (127) | 6 | $-11578.88 | -6.1% |
| **+20¢** | 26776 | 18637 | 8139 (166) | 7 | $-10235.91 | -6.1% |
| **+10¢ (15¢ stop)** | 58698 | 58605 | 93 (56) | 3 | $-21799.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 06:39 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-05 06:39 | +10 stop | HYPE | DOWN | 0.61 | open |  |
| 11-05 06:39 | +20 | HYPE | DOWN | 0.61 | open |  |
| 11-05 06:39 | +15 | HYPE | DOWN | 0.61 | open |  |
| 11-05 06:39 | +10 | HYPE | DOWN | 0.61 | open |  |
| 11-05 06:39 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-05 06:38 | +10 stop | ETH | DOWN | 0.57 | 0.67 | 0.66 |
| 11-05 06:38 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 11-05 06:37 | +10 stop | DOGE | UP | 0.45 | open |  |
| 11-05 06:36 | +5 | SOL | DOWN | 0.68 | open |  |
| 11-05 06:36 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.26 |
| 11-05 06:36 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-05 06:34 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 11-05 06:34 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 11-05 06:34 | +5 | ETH | DOWN | 0.56 | 0.65 | 0.56 |
| 11-05 06:34 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-05 06:33 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 11-05 06:33 | +10 stop | ETH | DOWN | 0.62 | 0.41 | -2.44 |
| 11-05 06:33 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-05 06:33 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-05 06:33 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-05 06:33 | +5 | ETH | DOWN | 0.62 | 0.68 | 0.27 |
| 11-05 06:33 | +5 | XRP | DOWN | 0.71 | 0.79 | 0.53 |
| 11-05 06:33 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 06:33 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-05 06:33 | +15 | XRP | DOWN | 0.71 | 0.88 | 1.47 |
| 11-05 06:33 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-05 06:32 | +10 stop | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-05 06:32 | +20 | ZEC | UP | 0.65 | 0.86 | 1.85 |
| 11-05 06:32 | +15 | ZEC | UP | 0.65 | 0.80 | 1.22 |
| 11-05 06:32 | +10 | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-05 06:32 | +5 | ZEC | UP | 0.65 | 0.76 | 0.81 |
| 11-05 06:32 | +10 stop | DOGE | UP | 0.65 | 0.49 | -1.94 |
| 11-05 06:32 | +20 | DOGE | UP | 0.65 | open |  |
| 11-05 06:32 | +15 | DOGE | UP | 0.66 | open |  |
| 11-05 06:32 | +10 | DOGE | UP | 0.66 | open |  |
| 11-05 06:32 | +5 | DOGE | UP | 0.66 | open |  |
| 11-05 06:32 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.93 |
| 11-05 06:32 | +20 | NEAR | UP | 0.70 | open |  |
| 11-05 06:32 | +15 | NEAR | UP | 0.70 | open |  |
