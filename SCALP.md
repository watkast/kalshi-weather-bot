# Range-Scalp Bot

*Updated Tue Oct 13 11:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14557 | 12587 | 1970 (27) | 0 | $-4715.42 | -5.1% |
| **+10¢** | 11017 | 8730 | 2287 (39) | 0 | $-4425.51 | -6.4% |
| **+15¢** | 9258 | 6812 | 2446 (57) | 4 | $-3938.73 | -6.8% |
| **+20¢** | 8238 | 5692 | 2546 (72) | 6 | $-3384.28 | -6.5% |
| **+10¢ (15¢ stop)** | 17868 | 17819 | 49 (29) | 0 | $-6948.05 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 11:18 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-13 11:18 | +10 | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 10-13 11:18 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.61 |
| 10-13 11:17 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 11:17 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-13 11:17 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.50 |
| 10-13 11:17 | +10 stop | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 11:17 | +10 | BTC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-13 11:17 | +5 | BTC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-13 11:16 | +10 stop | XRP | DOWN | 0.66 | 0.51 | -1.84 |
| 10-13 11:16 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-13 11:16 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-13 11:16 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 0.99 |
| 10-13 11:16 | +20 | HYPE | DOWN | 0.68 | open |  |
| 10-13 11:16 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-13 11:16 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-13 11:16 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 11:16 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +20 | SOL | DOWN | 0.66 | open |  |
| 10-13 11:16 | +15 | SOL | DOWN | 0.66 | 0.81 | 1.23 |
| 10-13 11:16 | +10 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-13 11:16 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 11:16 | +10 stop | BNB | UP | 0.45 | 0.57 | 0.84 |
| 10-13 11:16 | +20 | BNB | UP | 0.45 | open |  |
| 10-13 11:16 | +15 | BNB | UP | 0.45 | open |  |
| 10-13 11:16 | +10 | BNB | UP | 0.45 | 0.57 | 0.84 |
| 10-13 11:16 | +5 | BNB | UP | 0.45 | 0.57 | 0.84 |
| 10-13 11:16 | +10 stop | BTC | UP | 0.48 | 0.59 | 0.75 |
| 10-13 11:16 | +20 | BTC | UP | 0.48 | open |  |
| 10-13 11:16 | +15 | BTC | UP | 0.48 | open |  |
| 10-13 11:16 | +10 | BTC | UP | 0.48 | 0.59 | 0.75 |
| 10-13 11:16 | +5 | BTC | UP | 0.48 | 0.59 | 0.75 |
| 10-13 11:16 | +10 stop | ETH | UP | 0.40 | 0.53 | 0.95 |
| 10-13 11:16 | +20 | ETH | UP | 0.40 | open |  |
| 10-13 11:16 | +15 | ETH | UP | 0.40 | open |  |
| 10-13 11:16 | +10 | ETH | UP | 0.40 | 0.53 | 0.95 |
| 10-13 11:16 | +5 | ETH | UP | 0.40 | 0.53 | 0.95 |
| 10-13 11:02 | +10 stop | ETH | DOWN | 0.57 | 0.87 | 2.74 |
