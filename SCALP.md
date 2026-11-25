# Range-Scalp Bot

*Updated Wed Nov 25 17:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71814 | 62676 | 9138 (158) | 5 | $-19167.85 | -4.2% |
| **+10¢** | 53573 | 42904 | 10669 (203) | 5 | $-17752.03 | -5.3% |
| **+15¢** | 44867 | 33375 | 11492 (260) | 6 | $-15838.94 | -5.6% |
| **+20¢** | 39949 | 27847 | 12102 (326) | 6 | $-14219.51 | -5.7% |
| **+10¢ (15¢ stop)** | 87451 | 87242 | 209 (128) | 5 | $-32105.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 17:23 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 11-25 17:23 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 11-25 17:23 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 11-25 17:23 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-25 17:23 | +5 | BTC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-25 17:23 | +10 stop | HYPE | UP | 0.68 | 0.47 | -2.44 |
| 11-25 17:23 | +10 | HYPE | UP | 0.68 | open |  |
| 11-25 17:23 | +5 | HYPE | UP | 0.69 | open |  |
| 11-25 17:23 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-25 17:23 | +10 | XRP | UP | 0.71 | open |  |
| 11-25 17:23 | +5 | XRP | UP | 0.71 | open |  |
| 11-25 17:23 | +10 stop | SOL | UP | 0.64 | open |  |
| 11-25 17:23 | +20 | SOL | UP | 0.63 | open |  |
| 11-25 17:23 | +15 | SOL | UP | 0.63 | open |  |
| 11-25 17:23 | +10 | SOL | UP | 0.64 | open |  |
| 11-25 17:23 | +5 | SOL | UP | 0.64 | open |  |
| 11-25 17:22 | +10 stop | BNB | UP | 0.57 | 0.42 | -1.86 |
| 11-25 17:22 | +10 | BNB | UP | 0.57 | open |  |
| 11-25 17:22 | +5 | BNB | UP | 0.57 | open |  |
| 11-25 17:22 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-25 17:22 | +15 | ETH | UP | 0.62 | open |  |
| 11-25 17:22 | +10 | ETH | UP | 0.63 | open |  |
| 11-25 17:22 | +5 | ETH | UP | 0.63 | open |  |
| 11-25 17:21 | +10 stop | BTC | UP | 0.63 | 0.78 | 1.20 |
| 11-25 17:21 | +20 | BTC | UP | 0.63 | open |  |
| 11-25 17:21 | +15 | BTC | UP | 0.64 | open |  |
| 11-25 17:21 | +10 | BTC | UP | 0.64 | 0.78 | 1.10 |
| 11-25 17:21 | +5 | BTC | UP | 0.64 | 0.78 | 1.10 |
| 11-25 17:21 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-25 17:21 | +20 | XRP | UP | 0.68 | open |  |
| 11-25 17:21 | +15 | XRP | UP | 0.67 | open |  |
| 11-25 17:21 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-25 17:21 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 11-25 17:21 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-25 17:21 | +15 | HYPE | UP | 0.67 | open |  |
| 11-25 17:21 | +10 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-25 17:21 | +5 | HYPE | UP | 0.67 | 0.79 | 0.92 |
| 11-25 17:21 | +10 stop | ETH | UP | 0.58 | 0.76 | 1.49 |
| 11-25 17:21 | +20 | ETH | UP | 0.58 | open |  |
| 11-25 17:21 | +15 | ETH | UP | 0.57 | 0.76 | 1.59 |
