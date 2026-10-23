# Range-Scalp Bot

*Updated Fri Oct 23 03:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29688 | 25836 | 3852 (39) | 1 | $-8806.22 | -4.7% |
| **+10¢** | 22261 | 17801 | 4460 (55) | 1 | $-7942.93 | -5.7% |
| **+15¢** | 18643 | 13855 | 4788 (78) | 1 | $-7119.71 | -6.1% |
| **+20¢** | 16500 | 11483 | 5017 (100) | 1 | $-6445.62 | -6.2% |
| **+10¢ (15¢ stop)** | 36434 | 36375 | 59 (32) | 1 | $-13737.14 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 03:24 | +10 stop | HYPE | DOWN | 0.63 | open |  |
| 10-23 03:24 | +15 | HYPE | DOWN | 0.63 | open |  |
| 10-23 03:24 | +10 | HYPE | DOWN | 0.63 | open |  |
| 10-23 03:24 | +5 | HYPE | DOWN | 0.63 | open |  |
| 10-23 03:23 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-23 03:23 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-23 03:23 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-23 03:23 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-23 03:23 | +5 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 10-23 03:16 | +10 stop | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 10-23 03:16 | +20 | NEAR | DOWN | 0.70 | 0.93 | 2.14 |
| 10-23 03:16 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-23 03:16 | +10 | NEAR | DOWN | 0.70 | 0.84 | 1.15 |
| 10-23 03:16 | +5 | NEAR | DOWN | 0.70 | 0.78 | 0.52 |
| 10-23 03:15 | +10 stop | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-23 03:15 | +20 | SOL | DOWN | 0.62 | 0.83 | 1.83 |
| 10-23 03:15 | +15 | SOL | DOWN | 0.62 | 0.78 | 1.30 |
| 10-23 03:15 | +10 | SOL | DOWN | 0.62 | 0.75 | 0.99 |
| 10-23 03:15 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 10-23 03:06 | +10 stop | ZEC | DOWN | 0.62 | 0.41 | -2.44 |
| 10-23 03:04 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 10-23 03:04 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-23 03:04 | +10 stop | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-23 03:04 | +10 | NEAR | DOWN | 0.61 | 0.74 | 0.99 |
| 10-23 03:04 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 10-23 03:03 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-23 03:03 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-23 03:03 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 10-23 03:03 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 10-23 03:03 | +10 stop | HYPE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-23 03:03 | +10 stop | DOGE | DOWN | 0.60 | 0.75 | 1.17 |
| 10-23 03:03 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 03:02 | +10 stop | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 10-23 03:02 | +20 | SOL | DOWN | 0.62 | 0.87 | 2.25 |
| 10-23 03:02 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 10-23 03:02 | +10 | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 10-23 03:02 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 10-23 03:02 | +10 stop | ETH | UP | 0.40 | 0.54 | 1.05 |
| 10-23 03:02 | +5 | ETH | UP | 0.40 | 0.54 | 1.05 |
| 10-23 03:02 | +10 stop | NEAR | DOWN | 0.55 | 0.68 | 0.96 |
