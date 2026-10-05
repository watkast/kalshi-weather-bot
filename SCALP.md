# Range-Scalp Bot

*Updated Mon Oct 05 00:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3042 | 2607 | 435 (3) | 6 | $-1130.24 | -5.9% |
| **+10¢** | 2360 | 1870 | 490 (4) | 7 | $-972.85 | -6.5% |
| **+15¢** | 1989 | 1472 | 517 (5) | 7 | $-845.67 | -6.8% |
| **+20¢** | 1775 | 1236 | 539 (10) | 7 | $-713.07 | -6.4% |
| **+10¢ (15¢ stop)** | 3813 | 3812 | 1 (1) | 3 | $-1541.62 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 00:52 | +10 stop | NEAR | UP | 0.62 | open |  |
| 10-05 00:52 | +10 stop | SOL | DOWN | 0.68 | 0.50 | -2.14 |
| 10-05 00:52 | +10 stop | ETH | UP | 0.63 | open |  |
| 10-05 00:51 | +10 stop | BTC | UP | 0.65 | open |  |
| 10-05 00:51 | +5 | BTC | UP | 0.65 | open |  |
| 10-05 00:51 | +10 stop | BTC | DOWN | 0.40 | 0.54 | 1.05 |
| 10-05 00:51 | +5 | BTC | DOWN | 0.40 | 0.54 | 1.05 |
| 10-05 00:50 | +10 stop | NEAR | UP | 0.64 | 0.78 | 1.10 |
| 10-05 00:50 | +5 | SOL | DOWN | 0.60 | open |  |
| 10-05 00:49 | +10 stop | BNB | UP | 0.62 | 0.78 | 1.30 |
| 10-05 00:48 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 10-05 00:48 | +10 stop | SOL | UP | 0.52 | 0.36 | -1.95 |
| 10-05 00:48 | +20 | SOL | UP | 0.52 | open |  |
| 10-05 00:48 | +15 | SOL | UP | 0.52 | open |  |
| 10-05 00:48 | +10 | SOL | UP | 0.52 | open |  |
| 10-05 00:48 | +5 | SOL | UP | 0.52 | 0.57 | 0.14 |
| 10-05 00:48 | +5 | BTC | DOWN | 0.50 | 0.57 | 0.34 |
| 10-05 00:48 | +10 stop | NEAR | DOWN | 0.53 | 0.37 | -1.95 |
| 10-05 00:48 | +15 | NEAR | DOWN | 0.53 | open |  |
| 10-05 00:48 | +10 | NEAR | DOWN | 0.53 | open |  |
| 10-05 00:48 | +5 | NEAR | DOWN | 0.53 | open |  |
| 10-05 00:48 | +10 stop | HYPE | UP | 0.69 | 0.83 | 1.11 |
| 10-05 00:47 | +10 stop | DOGE | DOWN | 0.49 | 0.29 | -2.33 |
| 10-05 00:47 | +20 | DOGE | DOWN | 0.48 | open |  |
| 10-05 00:47 | +15 | DOGE | DOWN | 0.48 | open |  |
| 10-05 00:47 | +10 | DOGE | DOWN | 0.48 | open |  |
| 10-05 00:47 | +5 | DOGE | DOWN | 0.48 | 0.55 | 0.34 |
| 10-05 00:47 | +5 | BNB | DOWN | 0.53 | open |  |
| 10-05 00:47 | +5 | ETH | DOWN | 0.66 | open |  |
| 10-05 00:46 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 10-05 00:46 | +20 | XRP | UP | 0.69 | 0.90 | 1.92 |
| 10-05 00:46 | +15 | XRP | UP | 0.69 | 0.84 | 1.25 |
| 10-05 00:46 | +10 | XRP | UP | 0.69 | 0.80 | 0.83 |
| 10-05 00:46 | +5 | XRP | UP | 0.69 | 0.75 | 0.31 |
| 10-05 00:46 | +10 stop | BTC | DOWN | 0.66 | 0.49 | -2.04 |
| 10-05 00:46 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-05 00:46 | +15 | BTC | DOWN | 0.66 | open |  |
| 10-05 00:46 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-05 00:46 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-05 00:46 | +10 stop | BNB | DOWN | 0.49 | 0.32 | -2.04 |
