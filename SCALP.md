# Range-Scalp Bot

*Updated Sat Nov 14 02:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58904 | 51392 | 7512 (106) | 3 | $-15932.15 | -4.3% |
| **+10¢** | 44010 | 35227 | 8783 (139) | 4 | $-14898.15 | -5.4% |
| **+15¢** | 36878 | 27412 | 9466 (174) | 5 | $-13515.22 | -5.8% |
| **+20¢** | 32853 | 22914 | 9939 (226) | 5 | $-11907.16 | -5.8% |
| **+10¢ (15¢ stop)** | 71730 | 71592 | 138 (82) | 0 | $-26388.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 02:32 | +10 stop | SOL | UP | 0.71 | 0.48 | -2.63 |
| 11-14 02:32 | +5 | BNB | UP | 0.70 | 0.75 | 0.21 |
| 11-14 02:32 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-14 02:32 | +10 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 11-14 02:32 | +5 | BTC | UP | 0.65 | 0.73 | 0.50 |
| 11-14 02:31 | +10 stop | HYPE | DOWN | 0.54 | 0.26 | -3.12 |
| 11-14 02:31 | +20 | HYPE | DOWN | 0.55 | open |  |
| 11-14 02:31 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-14 02:31 | +10 | HYPE | DOWN | 0.54 | open |  |
| 11-14 02:31 | +5 | HYPE | DOWN | 0.55 | open |  |
| 11-14 02:31 | +10 stop | BNB | DOWN | 0.52 | 0.35 | -2.03 |
| 11-14 02:31 | +20 | BNB | DOWN | 0.51 | open |  |
| 11-14 02:31 | +15 | BNB | DOWN | 0.50 | open |  |
| 11-14 02:31 | +10 | BNB | DOWN | 0.50 | open |  |
| 11-14 02:31 | +5 | BNB | DOWN | 0.50 | 0.56 | 0.24 |
| 11-14 02:31 | +10 stop | NEAR | DOWN | 0.55 | 0.37 | -2.15 |
| 11-14 02:31 | +20 | NEAR | DOWN | 0.55 | open |  |
| 11-14 02:31 | +15 | NEAR | DOWN | 0.55 | open |  |
| 11-14 02:31 | +10 | NEAR | DOWN | 0.55 | open |  |
| 11-14 02:31 | +5 | NEAR | DOWN | 0.55 | open |  |
| 11-14 02:31 | +10 stop | BTC | DOWN | 0.42 | 0.54 | 0.84 |
| 11-14 02:31 | +20 | BTC | DOWN | 0.42 | open |  |
| 11-14 02:31 | +15 | BTC | DOWN | 0.42 | open |  |
| 11-14 02:31 | +10 | BTC | DOWN | 0.42 | 0.54 | 0.84 |
| 11-14 02:31 | +5 | BTC | DOWN | 0.42 | 0.54 | 0.84 |
| 11-14 02:31 | +10 stop | XRP | UP | 0.48 | 0.68 | 1.66 |
| 11-14 02:31 | +20 | XRP | UP | 0.50 | 0.73 | 1.98 |
| 11-14 02:31 | +15 | XRP | UP | 0.50 | 0.68 | 1.46 |
| 11-14 02:31 | +10 | XRP | UP | 0.49 | 0.68 | 1.56 |
| 11-14 02:31 | +5 | XRP | UP | 0.50 | 0.57 | 0.34 |
| 11-14 02:31 | +10 stop | SOL | DOWN | 0.68 | 0.48 | -2.34 |
| 11-14 02:31 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-14 02:31 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-14 02:31 | +10 | SOL | DOWN | 0.68 | open |  |
| 11-14 02:31 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-14 02:31 | +10 stop | ETH | UP | 0.47 | 0.60 | 0.95 |
| 11-14 02:31 | +20 | ETH | UP | 0.46 | 0.73 | 2.38 |
| 11-14 02:31 | +15 | ETH | UP | 0.49 | 0.73 | 2.08 |
| 11-14 02:31 | +10 | ETH | UP | 0.49 | 0.60 | 0.75 |
| 11-14 02:31 | +5 | ETH | UP | 0.49 | 0.60 | 0.75 |
