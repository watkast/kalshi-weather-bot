# Range-Scalp Bot

*Updated Wed Oct 28 11:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38005 | 33163 | 4842 (46) | 0 | $-10687.78 | -4.5% |
| **+10¢** | 28351 | 22747 | 5604 (68) | 0 | $-9562.59 | -5.4% |
| **+15¢** | 23719 | 17703 | 6016 (93) | 0 | $-8510.77 | -5.7% |
| **+20¢** | 21037 | 14737 | 6300 (118) | 0 | $-7482.10 | -5.7% |
| **+10¢ (15¢ stop)** | 46524 | 46457 | 67 (35) | 0 | $-17710.32 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 11:03 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-28 11:02 | +5 | XRP | DOWN | 0.59 | 0.67 | 0.47 |
| 10-28 11:02 | +10 stop | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-28 11:02 | +20 | BTC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-28 11:02 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-28 11:02 | +10 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-28 11:02 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-28 11:01 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 11:01 | +20 | ZEC | DOWN | 0.70 | 0.91 | 1.89 |
| 10-28 11:01 | +15 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-28 11:01 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.82 |
| 10-28 11:01 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.51 |
| 10-28 11:01 | +10 stop | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 11:01 | +20 | DOGE | DOWN | 0.64 | 0.87 | 2.05 |
| 10-28 11:01 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 11:01 | +10 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-28 11:01 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-28 11:01 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 10-28 11:01 | +20 | ETH | DOWN | 0.67 | 0.88 | 1.86 |
| 10-28 11:01 | +15 | ETH | DOWN | 0.67 | 0.82 | 1.23 |
| 10-28 11:01 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.00 |
| 10-28 11:01 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.27 |
| 10-28 11:01 | +10 stop | XRP | DOWN | 0.59 | 0.74 | 1.23 |
| 10-28 11:01 | +20 | XRP | DOWN | 0.59 | 0.82 | 2.06 |
| 10-28 11:01 | +15 | XRP | DOWN | 0.58 | 0.74 | 1.24 |
| 10-28 11:01 | +10 | XRP | DOWN | 0.58 | 0.74 | 1.24 |
| 10-28 11:01 | +5 | XRP | DOWN | 0.58 | 0.64 | 0.21 |
| 10-28 11:01 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.15 |
| 10-28 11:01 | +20 | HYPE | DOWN | 0.66 | 0.88 | 1.99 |
| 10-28 11:01 | +15 | HYPE | DOWN | 0.66 | 0.85 | 1.68 |
| 10-28 11:01 | +10 | HYPE | DOWN | 0.66 | 0.80 | 1.15 |
| 10-28 11:01 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.22 |
| 10-28 10:58 | +5 | XRP | UP | 0.57 | no | -5.84 |
| 10-28 10:57 | +10 stop | ETH | DOWN | 0.54 | 0.68 | 1.06 |
| 10-28 10:57 | +10 stop | XRP | UP | 0.60 | 0.08 | -5.42 |
| 10-28 10:57 | +20 | XRP | UP | 0.60 | no | -6.17 |
| 10-28 10:57 | +15 | XRP | UP | 0.60 | no | -6.17 |
| 10-28 10:57 | +10 | XRP | UP | 0.60 | no | -6.17 |
| 10-28 10:57 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 10-28 10:57 | +10 stop | SOL | UP | 0.66 | 0.25 | -4.40 |
