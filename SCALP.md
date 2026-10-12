# Range-Scalp Bot

*Updated Mon Oct 12 03:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12954 | 11182 | 1772 (25) | 2 | $-4281.68 | -5.2% |
| **+10¢** | 9824 | 7777 | 2047 (37) | 2 | $-3989.61 | -6.4% |
| **+15¢** | 8258 | 6074 | 2184 (55) | 5 | $-3499.35 | -6.7% |
| **+20¢** | 7354 | 5079 | 2275 (69) | 6 | $-2985.72 | -6.5% |
| **+10¢ (15¢ stop)** | 15972 | 15931 | 41 (25) | 0 | $-6291.00 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 03:05 | +10 stop | NEAR | UP | 0.61 | 0.45 | -1.95 |
| 10-12 03:04 | +10 stop | NEAR | UP | 0.71 | 0.52 | -2.23 |
| 10-12 03:03 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.74 |
| 10-12 03:03 | +5 | ZEC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-12 03:03 | +10 stop | DOGE | DOWN | 0.62 | 0.75 | 0.95 |
| 10-12 03:03 | +20 | DOGE | DOWN | 0.62 | open |  |
| 10-12 03:03 | +15 | DOGE | DOWN | 0.62 | 0.80 | 1.51 |
| 10-12 03:03 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-12 03:03 | +5 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 10-12 03:03 | +10 stop | ZEC | DOWN | 0.60 | 0.44 | -1.95 |
| 10-12 03:03 | +20 | ZEC | DOWN | 0.60 | open |  |
| 10-12 03:03 | +15 | ZEC | DOWN | 0.60 | open |  |
| 10-12 03:03 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 10-12 03:03 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 10-12 03:02 | +10 stop | NEAR | DOWN | 0.63 | 0.34 | -3.23 |
| 10-12 03:02 | +20 | NEAR | DOWN | 0.63 | open |  |
| 10-12 03:02 | +15 | NEAR | DOWN | 0.63 | open |  |
| 10-12 03:02 | +10 | NEAR | DOWN | 0.63 | open |  |
| 10-12 03:02 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-12 03:02 | +5 | HYPE | DOWN | 0.60 | open |  |
| 10-12 03:01 | +10 stop | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 03:01 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-12 03:01 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-12 03:01 | +10 | ETH | DOWN | 0.69 | 0.79 | 0.73 |
| 10-12 03:01 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-12 03:01 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-12 03:01 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-12 03:01 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-12 03:01 | +10 | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 10-12 03:01 | +5 | XRP | DOWN | 0.71 | 0.77 | 0.32 |
| 10-12 03:01 | +10 stop | HYPE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-12 03:01 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-12 03:01 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-12 03:01 | +10 | HYPE | DOWN | 0.66 | open |  |
| 10-12 03:01 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-12 02:58 | +10 stop | BNB | DOWN | 0.54 | 0.67 | 0.96 |
| 10-12 02:58 | +5 | BNB | DOWN | 0.54 | 0.59 | 0.15 |
| 10-12 02:58 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.83 |
| 10-12 02:56 | +10 stop | SOL | UP | 0.63 | 0.34 | -3.23 |
| 10-12 02:56 | +15 | SOL | UP | 0.63 | no | -6.47 |
