# Range-Scalp Bot

*Updated Tue Oct 20 21:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 26248 | 22859 | 3389 (32) | 2 | $-7677.29 | -4.6% |
| **+10¢** | 19753 | 15838 | 3915 (47) | 2 | $-6776.63 | -5.5% |
| **+15¢** | 16532 | 12319 | 4213 (71) | 3 | $-6054.05 | -5.8% |
| **+20¢** | 14629 | 10212 | 4417 (90) | 3 | $-5445.53 | -5.9% |
| **+10¢ (15¢ stop)** | 32151 | 32098 | 53 (30) | 0 | $-11762.26 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 21:35 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-20 21:33 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.44 |
| 10-20 21:33 | +5 | SOL | DOWN | 0.67 | 0.72 | 0.19 |
| 10-20 21:32 | +5 | HYPE | UP | 0.60 | open |  |
| 10-20 21:32 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-20 21:32 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.83 |
| 10-20 21:32 | +15 | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 21:32 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-20 21:32 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-20 21:31 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.82 |
| 10-20 21:31 | +20 | SOL | DOWN | 0.69 | open |  |
| 10-20 21:31 | +15 | SOL | DOWN | 0.69 | open |  |
| 10-20 21:31 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.82 |
| 10-20 21:31 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.30 |
| 10-20 21:31 | +10 stop | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 21:31 | +20 | DOGE | DOWN | 0.67 | 0.88 | 1.86 |
| 10-20 21:31 | +15 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 21:31 | +10 | DOGE | DOWN | 0.67 | 0.82 | 1.23 |
| 10-20 21:31 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 10-20 21:31 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 21:31 | +20 | BNB | DOWN | 0.60 | 0.82 | 1.92 |
| 10-20 21:31 | +15 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-20 21:31 | +10 | BNB | DOWN | 0.60 | 0.76 | 1.30 |
| 10-20 21:31 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 10-20 21:31 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.04 |
| 10-20 21:31 | +20 | HYPE | UP | 0.67 | open |  |
| 10-20 21:31 | +15 | HYPE | UP | 0.67 | open |  |
| 10-20 21:31 | +10 | HYPE | UP | 0.67 | open |  |
| 10-20 21:31 | +5 | HYPE | UP | 0.63 | 0.69 | 0.28 |
| 10-20 21:31 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 10-20 21:31 | +20 | ZEC | UP | 0.61 | open |  |
| 10-20 21:31 | +15 | ZEC | UP | 0.61 | open |  |
| 10-20 21:31 | +10 | ZEC | UP | 0.62 | open |  |
| 10-20 21:31 | +5 | ZEC | UP | 0.62 | open |  |
| 10-20 21:31 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 21:31 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 10-20 21:31 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 10-20 21:31 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 10-20 21:31 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-20 21:31 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
