# Range-Scalp Bot

*Updated Wed Nov 18 09:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63900 | 55731 | 8169 (119) | 2 | $-17472.14 | -4.3% |
| **+10¢** | 47739 | 38176 | 9563 (160) | 2 | $-16391.01 | -5.5% |
| **+15¢** | 40030 | 29720 | 10310 (205) | 2 | $-14854.01 | -5.9% |
| **+20¢** | 35650 | 24827 | 10823 (260) | 3 | $-13159.02 | -5.9% |
| **+10¢ (15¢ stop)** | 77736 | 77578 | 158 (93) | 1 | $-28537.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 09:11 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-18 09:11 | +20 | ETH | UP | 0.60 | open |  |
| 11-18 09:11 | +15 | ETH | UP | 0.60 | open |  |
| 11-18 09:11 | +10 | ETH | UP | 0.60 | open |  |
| 11-18 09:11 | +5 | ETH | UP | 0.60 | open |  |
| 11-18 09:11 | +10 stop | ZEC | UP | 0.37 | 0.63 | 2.26 |
| 11-18 09:11 | +20 | ZEC | UP | 0.37 | 0.63 | 2.26 |
| 11-18 09:11 | +15 | ZEC | UP | 0.36 | 0.63 | 2.34 |
| 11-18 09:11 | +10 | ZEC | UP | 0.36 | 0.63 | 2.34 |
| 11-18 09:11 | +5 | ZEC | UP | 0.37 | 0.63 | 2.26 |
| 11-18 09:10 | +10 stop | XRP | DOWN | 0.58 | 0.83 | 2.22 |
| 11-18 09:09 | +5 | XRP | UP | 0.68 | open |  |
| 11-18 09:08 | +5 | XRP | UP | 0.56 | 0.62 | 0.25 |
| 11-18 09:07 | +10 stop | XRP | DOWN | 0.49 | 0.30 | -2.23 |
| 11-18 09:07 | +5 | XRP | DOWN | 0.49 | 0.55 | 0.24 |
| 11-18 09:06 | +5 | XRP | UP | 0.58 | 0.65 | 0.36 |
| 11-18 09:05 | +5 | XRP | UP | 0.61 | 0.69 | 0.48 |
| 11-18 09:04 | +5 | XRP | UP | 0.64 | 0.70 | 0.30 |
| 11-18 09:01 | +10 stop | XRP | UP | 0.66 | 0.49 | -2.04 |
| 11-18 09:01 | +20 | XRP | UP | 0.68 | open |  |
| 11-18 09:01 | +15 | XRP | UP | 0.68 | open |  |
| 11-18 09:01 | +10 | XRP | UP | 0.68 | open |  |
| 11-18 09:01 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 11-18 09:01 | +10 stop | HYPE | UP | 0.70 | 0.81 | 0.82 |
| 11-18 09:01 | +20 | HYPE | UP | 0.71 | 0.93 | 2.02 |
| 11-18 09:01 | +15 | HYPE | UP | 0.71 | 0.89 | 1.58 |
| 11-18 09:01 | +10 | HYPE | UP | 0.70 | 0.81 | 0.84 |
| 11-18 09:01 | +5 | HYPE | UP | 0.70 | 0.76 | 0.32 |
| 11-18 09:01 | +10 stop | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-18 09:01 | +20 | BTC | UP | 0.71 | open |  |
| 11-18 09:01 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-18 09:01 | +10 | BTC | UP | 0.71 | 0.81 | 0.74 |
| 11-18 09:01 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-18 08:54 | +10 stop | NEAR | DOWN | 0.70 | 0.82 | 0.91 |
| 11-18 08:54 | +10 stop | DOGE | UP | 0.40 | 0.54 | 1.05 |
| 11-18 08:54 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-18 08:54 | +10 stop | HYPE | DOWN | 0.59 | 0.87 | 2.55 |
| 11-18 08:53 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-18 08:53 | +10 stop | ETH | UP | 0.60 | 0.37 | -2.64 |
| 11-18 08:53 | +20 | ETH | UP | 0.60 | no | -6.17 |
