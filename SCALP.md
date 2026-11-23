# Range-Scalp Bot

*Updated Mon Nov 23 03:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69569 | 60704 | 8865 (146) | 2 | $-18721.48 | -4.3% |
| **+10¢** | 51909 | 41553 | 10356 (189) | 3 | $-17414.76 | -5.3% |
| **+15¢** | 43496 | 32340 | 11156 (244) | 4 | $-15561.20 | -5.7% |
| **+20¢** | 38734 | 27005 | 11729 (306) | 5 | $-13873.62 | -5.7% |
| **+10¢ (15¢ stop)** | 84682 | 84492 | 190 (118) | 0 | $-31094.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 03:57 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-23 03:57 | +10 stop | SOL | UP | 0.65 | 0.91 | 2.36 |
| 11-23 03:57 | +20 | SOL | UP | 0.65 | 0.91 | 2.36 |
| 11-23 03:57 | +15 | SOL | UP | 0.65 | 0.91 | 2.36 |
| 11-23 03:57 | +10 | SOL | UP | 0.65 | 0.91 | 2.36 |
| 11-23 03:57 | +5 | SOL | UP | 0.67 | 0.91 | 2.16 |
| 11-23 03:56 | +10 stop | XRP | DOWN | 0.58 | 0.37 | -2.45 |
| 11-23 03:56 | +20 | XRP | DOWN | 0.58 | open |  |
| 11-23 03:56 | +15 | XRP | DOWN | 0.58 | open |  |
| 11-23 03:56 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-23 03:56 | +5 | XRP | DOWN | 0.56 | 0.61 | 0.15 |
| 11-23 03:56 | +10 stop | ETH | UP | 0.65 | 0.80 | 1.22 |
| 11-23 03:56 | +20 | ETH | UP | 0.64 | open |  |
| 11-23 03:56 | +15 | ETH | UP | 0.64 | 0.80 | 1.31 |
| 11-23 03:56 | +10 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 11-23 03:56 | +5 | ETH | UP | 0.65 | 0.80 | 1.22 |
| 11-23 03:56 | +10 stop | SOL | DOWN | 0.29 | 0.53 | 2.07 |
| 11-23 03:56 | +20 | SOL | DOWN | 0.29 | 0.53 | 2.07 |
| 11-23 03:56 | +15 | SOL | DOWN | 0.29 | 0.53 | 2.07 |
| 11-23 03:56 | +10 | SOL | DOWN | 0.29 | 0.53 | 2.07 |
| 11-23 03:56 | +5 | SOL | DOWN | 0.29 | 0.53 | 2.07 |
| 11-23 03:55 | +10 stop | HYPE | DOWN | 0.53 | 0.22 | -3.41 |
| 11-23 03:55 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-23 03:55 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-23 03:55 | +5 | HYPE | DOWN | 0.53 | 0.59 | 0.29 |
| 11-23 03:55 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-23 03:55 | +10 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-23 03:55 | +5 | DOGE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-23 03:54 | +10 stop | BTC | DOWN | 0.67 | 0.48 | -2.24 |
| 11-23 03:54 | +10 | BTC | DOWN | 0.67 | open |  |
| 11-23 03:54 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-23 03:53 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 03:52 | +10 stop | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-23 03:52 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-23 03:52 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 11-23 03:52 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-23 03:51 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-23 03:51 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-23 03:51 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-23 03:50 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
