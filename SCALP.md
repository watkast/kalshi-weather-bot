# Range-Scalp Bot

*Updated Wed Oct 28 00:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37319 | 32580 | 4739 (45) | 1 | $-10380.87 | -4.4% |
| **+10¢** | 27866 | 22376 | 5490 (67) | 1 | $-9273.81 | -5.3% |
| **+15¢** | 23317 | 17419 | 5898 (91) | 1 | $-8247.17 | -5.6% |
| **+20¢** | 20666 | 14494 | 6172 (116) | 1 | $-7211.75 | -5.6% |
| **+10¢ (15¢ stop)** | 45718 | 45653 | 65 (34) | 1 | $-17443.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 00:45 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-28 00:45 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-28 00:45 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 10-28 00:45 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-28 00:45 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-28 00:42 | +10 stop | BTC | UP | 0.70 | 0.14 | -5.84 |
| 10-28 00:41 | +10 stop | DOGE | DOWN | 0.57 | 0.19 | -4.09 |
| 10-28 00:41 | +10 | DOGE | DOWN | 0.57 | 0.85 | 2.53 |
| 10-28 00:41 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 10-28 00:41 | +10 stop | BTC | DOWN | 0.69 | 0.48 | -2.43 |
| 10-28 00:40 | +10 stop | BTC | UP | 0.60 | 0.44 | -1.95 |
| 10-28 00:40 | +5 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 10-28 00:40 | +10 | ETH | UP | 0.66 | 0.82 | 1.33 |
| 10-28 00:40 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 10-28 00:39 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 00:39 | +15 | BNB | DOWN | 0.65 | yes | -6.66 |
| 10-28 00:39 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 00:39 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 10-28 00:39 | +10 stop | SOL | UP | 0.71 | 0.86 | 1.26 |
| 10-28 00:39 | +10 stop | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-28 00:38 | +10 stop | NEAR | UP | 0.65 | 0.80 | 1.22 |
| 10-28 00:38 | +10 stop | BTC | UP | 0.64 | 0.46 | -2.15 |
| 10-28 00:37 | +10 stop | SOL | DOWN | 0.66 | 0.46 | -2.34 |
| 10-28 00:37 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.85 |
| 10-28 00:37 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 10-28 00:37 | +5 | XRP | UP | 0.67 | 0.76 | 0.61 |
| 10-28 00:37 | +10 stop | ETH | DOWN | 0.68 | 0.42 | -2.94 |
| 10-28 00:37 | +10 stop | HYPE | UP | 0.55 | 0.65 | 0.66 |
| 10-28 00:36 | +5 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 10-28 00:36 | +10 stop | SOL | DOWN | 0.48 | 0.64 | 1.25 |
| 10-28 00:36 | +10 stop | ETH | DOWN | 0.45 | 0.57 | 0.84 |
| 10-28 00:36 | +10 stop | NEAR | UP | 0.57 | 0.42 | -1.86 |
| 10-28 00:36 | +10 stop | BNB | DOWN | 0.68 | 0.80 | 0.92 |
| 10-28 00:36 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 10-28 00:36 | +10 | BTC | UP | 0.64 | 0.75 | 0.79 |
| 10-28 00:36 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 10-28 00:36 | +5 | NEAR | UP | 0.56 | 0.64 | 0.45 |
| 10-28 00:35 | +5 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 10-28 00:35 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 10-28 00:35 | +5 | ETH | UP | 0.59 | 0.64 | 0.16 |
