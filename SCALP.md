# Range-Scalp Bot

*Updated Thu Nov 12 14:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57043 | 49724 | 7319 (101) | 4 | $-15707.14 | -4.4% |
| **+10¢** | 42634 | 34096 | 8538 (133) | 5 | $-14638.58 | -5.5% |
| **+15¢** | 35743 | 26555 | 9188 (167) | 5 | $-13229.84 | -5.9% |
| **+20¢** | 31844 | 22205 | 9639 (217) | 6 | $-11595.71 | -5.8% |
| **+10¢ (15¢ stop)** | 69565 | 69437 | 128 (78) | 1 | $-25711.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 14:57 | +10 stop | XRP | DOWN | 0.38 | 0.55 | 1.35 |
| 11-12 14:57 | +20 | XRP | DOWN | 0.42 | open |  |
| 11-12 14:57 | +15 | XRP | DOWN | 0.39 | 0.55 | 1.25 |
| 11-12 14:57 | +10 | XRP | DOWN | 0.37 | 0.55 | 1.49 |
| 11-12 14:57 | +5 | XRP | DOWN | 0.37 | 0.55 | 1.49 |
| 11-12 14:57 | +10 stop | ETH | UP | 0.56 | open |  |
| 11-12 14:57 | +20 | ETH | UP | 0.57 | open |  |
| 11-12 14:57 | +15 | ETH | UP | 0.57 | open |  |
| 11-12 14:57 | +10 | ETH | UP | 0.57 | open |  |
| 11-12 14:57 | +5 | ETH | UP | 0.53 | 0.65 | 0.83 |
| 11-12 14:56 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.00 |
| 11-12 14:56 | +10 stop | SOL | DOWN | 0.45 | 0.55 | 0.66 |
| 11-12 14:55 | +10 stop | HYPE | DOWN | 0.58 | 0.29 | -3.20 |
| 11-12 14:55 | +10 stop | ETH | DOWN | 0.51 | 0.31 | -2.33 |
| 11-12 14:54 | +10 stop | DOGE | UP | 0.46 | 0.18 | -3.09 |
| 11-12 14:54 | +10 stop | BNB | DOWN | 0.65 | 0.83 | 1.55 |
| 11-12 14:54 | +10 | BNB | DOWN | 0.65 | 0.83 | 1.54 |
| 11-12 14:54 | +5 | DOGE | UP | 0.58 | open |  |
| 11-12 14:53 | +10 | SOL | UP | 0.64 | open |  |
| 11-12 14:53 | +5 | SOL | UP | 0.63 | open |  |
| 11-12 14:53 | +5 | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 11-12 14:53 | +10 stop | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-12 14:52 | +5 | DOGE | UP | 0.53 | 0.61 | 0.45 |
| 11-12 14:52 | +10 stop | ETH | UP | 0.60 | 0.41 | -2.24 |
| 11-12 14:52 | +10 stop | DOGE | UP | 0.67 | 0.49 | -2.14 |
| 11-12 14:51 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-12 14:51 | +10 stop | ETH | DOWN | 0.56 | 0.36 | -2.35 |
| 11-12 14:51 | +10 stop | SOL | DOWN | 0.48 | 0.61 | 0.95 |
| 11-12 14:51 | +10 stop | BNB | DOWN | 0.58 | 0.26 | -3.52 |
| 11-12 14:51 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 11-12 14:50 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-12 14:50 | +20 | XRP | UP | 0.55 | 0.75 | 1.68 |
| 11-12 14:50 | +15 | XRP | UP | 0.54 | 0.75 | 1.78 |
| 11-12 14:50 | +10 | XRP | UP | 0.54 | 0.66 | 0.86 |
| 11-12 14:50 | +5 | XRP | UP | 0.54 | 0.62 | 0.45 |
| 11-12 14:50 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-12 14:49 | +10 stop | ETH | UP | 0.60 | 0.35 | -2.83 |
| 11-12 14:49 | +20 | ETH | UP | 0.60 | 0.80 | 1.71 |
| 11-12 14:49 | +15 | ETH | UP | 0.62 | 0.80 | 1.53 |
| 11-12 14:49 | +10 | ETH | UP | 0.62 | 0.80 | 1.53 |
