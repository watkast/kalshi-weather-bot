# Range-Scalp Bot

*Updated Sat Nov 21 06:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67147 | 58605 | 8542 (129) | 6 | $-18031.24 | -4.3% |
| **+10¢** | 50142 | 40157 | 9985 (171) | 6 | $-16763.24 | -5.3% |
| **+15¢** | 42045 | 31283 | 10762 (219) | 8 | $-15030.67 | -5.7% |
| **+20¢** | 37421 | 26112 | 11309 (276) | 8 | $-13368.53 | -5.7% |
| **+10¢ (15¢ stop)** | 81750 | 81584 | 166 (100) | 4 | $-30086.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 06:07 | +15 | ETH | UP | 0.51 | open |  |
| 11-21 06:07 | +10 | ETH | UP | 0.59 | open |  |
| 11-21 06:07 | +5 | ETH | UP | 0.59 | open |  |
| 11-21 06:06 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 11-21 06:06 | +5 | NEAR | DOWN | 0.62 | open |  |
| 11-21 06:05 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-21 06:05 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 11-21 06:05 | +10 stop | SOL | UP | 0.62 | 0.74 | 0.89 |
| 11-21 06:05 | +10 stop | ETH | DOWN | 0.52 | open |  |
| 11-21 06:05 | +5 | ETH | DOWN | 0.52 | 0.58 | 0.24 |
| 11-21 06:05 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
| 11-21 06:05 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-21 06:05 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-21 06:05 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-21 06:04 | +5 | NEAR | DOWN | 0.60 | 0.65 | 0.17 |
| 11-21 06:04 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.19 |
| 11-21 06:03 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 11-21 06:03 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-21 06:03 | +5 | XRP | DOWN | 0.66 | open |  |
| 11-21 06:03 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-21 06:03 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-21 06:03 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-21 06:03 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-21 06:03 | +10 | BTC | DOWN | 0.60 | open |  |
| 11-21 06:03 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-21 06:03 | +10 stop | ETH | UP | 0.44 | 0.54 | 0.64 |
| 11-21 06:03 | +20 | ETH | UP | 0.45 | open |  |
| 11-21 06:03 | +15 | ETH | UP | 0.45 | 0.61 | 1.25 |
| 11-21 06:03 | +10 | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-21 06:03 | +5 | ETH | UP | 0.45 | 0.54 | 0.54 |
| 11-21 06:02 | +5 | SOL | DOWN | 0.52 | 0.61 | 0.55 |
| 11-21 06:02 | +5 | XRP | DOWN | 0.56 | 0.67 | 0.76 |
| 11-21 06:02 | +5 | HYPE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-21 06:02 | +5 | DOGE | DOWN | 0.64 | 0.73 | 0.59 |
| 11-21 06:01 | +5 | NEAR | DOWN | 0.53 | 0.58 | 0.14 |
| 11-21 06:01 | +10 stop | SOL | DOWN | 0.52 | 0.37 | -1.85 |
| 11-21 06:01 | +20 | SOL | DOWN | 0.53 | open |  |
| 11-21 06:01 | +15 | SOL | DOWN | 0.53 | open |  |
| 11-21 06:01 | +10 | SOL | DOWN | 0.55 | open |  |
| 11-21 06:01 | +5 | SOL | DOWN | 0.55 | 0.61 | 0.25 |
