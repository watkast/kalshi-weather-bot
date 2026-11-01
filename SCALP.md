# Range-Scalp Bot

*Updated Sun Nov 01 01:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42999 | 37486 | 5513 (62) | 6 | $-12176.24 | -4.5% |
| **+10¢** | 32063 | 25691 | 6372 (84) | 7 | $-10920.09 | -5.4% |
| **+15¢** | 26819 | 19948 | 6871 (112) | 6 | $-10019.17 | -6.0% |
| **+20¢** | 23822 | 16624 | 7198 (145) | 7 | $-8854.02 | -5.9% |
| **+10¢ (15¢ stop)** | 52457 | 52374 | 83 (48) | 3 | $-19878.23 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 01:11 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-01 01:11 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-01 01:10 | +10 stop | SOL | DOWN | 0.65 | open |  |
| 11-01 01:10 | +5 | SOL | DOWN | 0.63 | open |  |
| 11-01 01:10 | +10 stop | BTC | UP | 0.59 | open |  |
| 11-01 01:10 | +10 | BTC | UP | 0.59 | open |  |
| 11-01 01:10 | +10 stop | BNB | UP | 0.51 | open |  |
| 11-01 01:10 | +5 | BNB | UP | 0.51 | 0.58 | 0.34 |
| 11-01 01:10 | +10 stop | DOGE | DOWN | 0.70 | 0.83 | 1.05 |
| 11-01 01:09 | +5 | BTC | UP | 0.69 | open |  |
| 11-01 01:09 | +10 stop | DOGE | DOWN | 0.44 | 0.56 | 0.84 |
| 11-01 01:09 | +10 stop | SOL | UP | 0.63 | 0.39 | -2.74 |
| 11-01 01:08 | +5 | XRP | DOWN | 0.69 | 0.85 | 1.40 |
| 11-01 01:08 | +10 stop | ZEC | UP | 0.68 | 0.46 | -2.54 |
| 11-01 01:08 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 11-01 01:08 | +5 | BTC | UP | 0.60 | 0.65 | 0.17 |
| 11-01 01:07 | +10 stop | DOGE | UP | 0.61 | 0.40 | -2.44 |
| 11-01 01:07 | +10 | DOGE | UP | 0.61 | open |  |
| 11-01 01:07 | +5 | DOGE | UP | 0.61 | open |  |
| 11-01 01:07 | +10 stop | XRP | DOWN | 0.63 | 0.85 | 1.94 |
| 11-01 01:07 | +10 | XRP | DOWN | 0.63 | 0.85 | 1.94 |
| 11-01 01:07 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-01 01:07 | +10 stop | BNB | UP | 0.62 | 0.77 | 1.20 |
| 11-01 01:05 | +10 stop | ETH | UP | 0.60 | 0.44 | -1.95 |
| 11-01 01:04 | +5 | BNB | UP | 0.61 | 0.70 | 0.53 |
| 11-01 01:04 | +5 | BTC | UP | 0.59 | 0.66 | 0.37 |
| 11-01 01:04 | +5 | BTC | UP | 0.54 | 0.65 | 0.76 |
| 11-01 01:04 | +10 stop | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-01 01:03 | +10 stop | HYPE | UP | 0.64 | 0.43 | -2.45 |
| 11-01 01:03 | +15 | HYPE | UP | 0.64 | open |  |
| 11-01 01:03 | +10 | HYPE | UP | 0.64 | open |  |
| 11-01 01:03 | +5 | HYPE | UP | 0.64 | open |  |
| 11-01 01:02 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-01 01:02 | +20 | BTC | UP | 0.58 | open |  |
| 11-01 01:02 | +15 | BTC | UP | 0.58 | open |  |
| 11-01 01:02 | +10 | BTC | UP | 0.58 | 0.69 | 0.77 |
| 11-01 01:02 | +5 | BTC | UP | 0.58 | 0.67 | 0.56 |
| 11-01 01:02 | +10 stop | ZEC | UP | 0.59 | 0.42 | -2.05 |
| 11-01 01:02 | +10 stop | DOGE | UP | 0.61 | 0.43 | -2.15 |
| 11-01 01:02 | +20 | DOGE | UP | 0.61 | open |  |
