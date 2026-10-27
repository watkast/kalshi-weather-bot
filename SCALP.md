# Range-Scalp Bot

*Updated Tue Oct 27 00:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35632 | 31092 | 4540 (43) | 4 | $-10007.39 | -4.5% |
| **+10¢** | 26644 | 21394 | 5250 (65) | 4 | $-8841.77 | -5.3% |
| **+15¢** | 22301 | 16656 | 5645 (89) | 6 | $-7903.42 | -5.6% |
| **+20¢** | 19768 | 13853 | 5915 (112) | 9 | $-6962.71 | -5.6% |
| **+10¢ (15¢ stop)** | 43687 | 43625 | 62 (33) | 4 | $-16651.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 00:03 | +10 stop | SOL | UP | 0.63 | open |  |
| 10-27 00:03 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-27 00:03 | +5 | BTC | UP | 0.70 | 0.79 | 0.63 |
| 10-27 00:03 | +10 stop | XRP | UP | 0.66 | open |  |
| 10-27 00:02 | +10 stop | XRP | DOWN | 0.41 | 0.59 | 1.46 |
| 10-27 00:02 | +10 stop | BTC | DOWN | 0.45 | 0.56 | 0.74 |
| 10-27 00:02 | +5 | BTC | DOWN | 0.45 | 0.56 | 0.74 |
| 10-27 00:02 | +10 stop | ETH | DOWN | 0.58 | 0.38 | -2.35 |
| 10-27 00:02 | +5 | HYPE | UP | 0.70 | open |  |
| 10-27 00:02 | +10 stop | SOL | DOWN | 0.63 | 0.48 | -1.85 |
| 10-27 00:02 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-27 00:02 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-27 00:02 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-27 00:02 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-27 00:01 | +10 stop | BTC | UP | 0.62 | 0.47 | -1.85 |
| 10-27 00:01 | +20 | BTC | UP | 0.62 | open |  |
| 10-27 00:01 | +15 | BTC | UP | 0.62 | 0.79 | 1.41 |
| 10-27 00:01 | +10 | BTC | UP | 0.61 | 0.74 | 0.99 |
| 10-27 00:01 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 10-27 00:01 | +10 stop | XRP | UP | 0.58 | 0.39 | -2.25 |
| 10-27 00:01 | +20 | XRP | UP | 0.58 | open |  |
| 10-27 00:01 | +15 | XRP | UP | 0.58 | open |  |
| 10-27 00:01 | +10 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 10-27 00:01 | +5 | XRP | UP | 0.58 | 0.63 | 0.15 |
| 10-27 00:01 | +10 stop | ETH | UP | 0.64 | 0.47 | -2.05 |
| 10-27 00:01 | +20 | ETH | UP | 0.64 | open |  |
| 10-27 00:01 | +15 | ETH | UP | 0.64 | open |  |
| 10-27 00:01 | +10 | ETH | UP | 0.62 | open |  |
| 10-27 00:01 | +5 | ETH | UP | 0.62 | open |  |
| 10-27 00:01 | +10 stop | ZEC | UP | 0.66 | 0.82 | 1.33 |
| 10-27 00:01 | +20 | ZEC | UP | 0.66 | open |  |
| 10-27 00:01 | +15 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 10-27 00:01 | +10 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 10-27 00:01 | +5 | ZEC | UP | 0.64 | 0.71 | 0.38 |
| 10-27 00:01 | +10 stop | BNB | UP | 0.70 | 0.81 | 0.84 |
| 10-27 00:01 | +20 | BNB | UP | 0.70 | open |  |
| 10-27 00:01 | +15 | BNB | UP | 0.70 | 0.88 | 1.57 |
| 10-27 00:01 | +10 | BNB | UP | 0.70 | 0.81 | 0.84 |
| 10-27 00:01 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 10-27 00:01 | +10 stop | HYPE | UP | 0.67 | open |  |
