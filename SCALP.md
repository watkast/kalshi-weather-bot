# Range-Scalp Bot

*Updated Mon Oct 12 18:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 13763 | 11921 | 1842 (25) | 1 | $-4309.31 | -5.0% |
| **+10¢** | 10417 | 8273 | 2144 (37) | 1 | $-4042.39 | -6.2% |
| **+15¢** | 8756 | 6462 | 2294 (55) | 1 | $-3581.29 | -6.5% |
| **+20¢** | 7789 | 5398 | 2391 (70) | 1 | $-3042.58 | -6.2% |
| **+10¢ (15¢ stop)** | 16901 | 16854 | 47 (27) | 0 | $-6612.88 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 18:29 | +10 stop | NEAR | DOWN | 0.61 | 0.03 | -5.96 |
| 10-12 18:29 | +15 | NEAR | DOWN | 0.61 | open |  |
| 10-12 18:29 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-12 18:29 | +5 | NEAR | DOWN | 0.63 | open |  |
| 10-12 18:27 | +10 stop | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 10-12 18:27 | +20 | NEAR | DOWN | 0.64 | open |  |
| 10-12 18:27 | +15 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 10-12 18:27 | +10 | NEAR | DOWN | 0.64 | 0.83 | 1.63 |
| 10-12 18:27 | +5 | NEAR | DOWN | 0.64 | 0.69 | 0.18 |
| 10-12 18:26 | +10 stop | NEAR | UP | 0.24 | 0.59 | 3.20 |
| 10-12 18:26 | +20 | NEAR | UP | 0.24 | 0.59 | 3.20 |
| 10-12 18:26 | +15 | NEAR | UP | 0.24 | 0.59 | 3.20 |
| 10-12 18:26 | +10 | NEAR | UP | 0.26 | 0.59 | 2.99 |
| 10-12 18:26 | +5 | NEAR | UP | 0.25 | 0.59 | 3.09 |
| 10-12 18:25 | +10 stop | BTC | DOWN | 0.61 | 0.87 | 2.35 |
| 10-12 18:25 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-12 18:24 | +10 stop | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-12 18:24 | +10 stop | BNB | DOWN | 0.62 | 0.76 | 1.10 |
| 10-12 18:23 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-12 18:23 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-12 18:23 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 10-12 18:21 | +10 stop | BNB | DOWN | 0.60 | 0.45 | -1.85 |
| 10-12 18:21 | +10 stop | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-12 18:21 | +20 | HYPE | DOWN | 0.58 | 0.84 | 2.32 |
| 10-12 18:21 | +15 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-12 18:21 | +10 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-12 18:21 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 10-12 18:21 | +10 stop | BTC | UP | 0.60 | 0.37 | -2.64 |
| 10-12 18:20 | +5 | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-12 18:20 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 10-12 18:19 | +10 stop | DOGE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-12 18:19 | +15 | DOGE | DOWN | 0.70 | 0.96 | 2.44 |
| 10-12 18:19 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-12 18:19 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-12 18:19 | +5 | ETH | DOWN | 0.61 | 0.66 | 0.17 |
| 10-12 18:18 | +10 | BNB | DOWN | 0.69 | 0.83 | 1.15 |
| 10-12 18:18 | +5 | BNB | DOWN | 0.69 | 0.76 | 0.42 |
| 10-12 18:17 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-12 18:17 | +20 | ETH | DOWN | 0.61 | 0.84 | 2.03 |
| 10-12 18:17 | +15 | ETH | DOWN | 0.61 | 0.80 | 1.61 |
