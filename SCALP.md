# Range-Scalp Bot

*Updated Wed Nov 11 14:18 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55922 | 48763 | 7159 (94) | 8 | $-15323.02 | -4.4% |
| **+10¢** | 41783 | 33434 | 8349 (124) | 9 | $-14264.30 | -5.4% |
| **+15¢** | 35040 | 26034 | 9006 (158) | 9 | $-13024.40 | -5.9% |
| **+20¢** | 31210 | 21762 | 9448 (208) | 9 | $-11398.78 | -5.8% |
| **+10¢ (15¢ stop)** | 68121 | 68000 | 121 (73) | 7 | $-25060.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 14:18 | +10 stop | BTC | UP | 0.59 | open |  |
| 11-11 14:18 | +10 stop | SOL | DOWN | 0.51 | open |  |
| 11-11 14:17 | +5 | DOGE | DOWN | 0.59 | open |  |
| 11-11 14:17 | +10 stop | HYPE | DOWN | 0.58 | open |  |
| 11-11 14:17 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-11 14:17 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-11 14:17 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-11 14:17 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-11 14:17 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 11-11 14:17 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-11 14:17 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-11 14:17 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-11 14:17 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.20 |
| 11-11 14:16 | +10 stop | DOGE | UP | 0.57 | 0.42 | -1.86 |
| 11-11 14:16 | +20 | DOGE | UP | 0.57 | open |  |
| 11-11 14:16 | +15 | DOGE | UP | 0.57 | open |  |
| 11-11 14:16 | +10 | DOGE | UP | 0.57 | open |  |
| 11-11 14:16 | +5 | DOGE | UP | 0.57 | 0.65 | 0.46 |
| 11-11 14:16 | +10 stop | ETH | UP | 0.68 | open |  |
| 11-11 14:16 | +20 | ETH | UP | 0.68 | open |  |
| 11-11 14:16 | +15 | ETH | UP | 0.68 | open |  |
| 11-11 14:16 | +10 | ETH | UP | 0.68 | open |  |
| 11-11 14:16 | +5 | ETH | UP | 0.68 | open |  |
| 11-11 14:16 | +10 stop | ZEC | UP | 0.59 | open |  |
| 11-11 14:16 | +20 | ZEC | UP | 0.60 | open |  |
| 11-11 14:16 | +15 | ZEC | UP | 0.60 | open |  |
| 11-11 14:16 | +10 | ZEC | UP | 0.61 | open |  |
| 11-11 14:16 | +5 | ZEC | UP | 0.61 | open |  |
| 11-11 14:16 | +10 stop | BTC | UP | 0.68 | 0.53 | -1.84 |
| 11-11 14:16 | +20 | BTC | UP | 0.68 | open |  |
| 11-11 14:16 | +15 | BTC | UP | 0.68 | open |  |
| 11-11 14:16 | +10 | BTC | UP | 0.68 | open |  |
| 11-11 14:16 | +5 | BTC | UP | 0.68 | open |  |
| 11-11 14:16 | +10 stop | BNB | UP | 0.67 | 0.50 | -2.04 |
| 11-11 14:16 | +20 | BNB | UP | 0.67 | open |  |
| 11-11 14:16 | +15 | BNB | UP | 0.67 | open |  |
| 11-11 14:16 | +10 | BNB | UP | 0.67 | open |  |
| 11-11 14:16 | +5 | BNB | UP | 0.67 | open |  |
| 11-11 14:16 | +10 stop | SOL | UP | 0.62 | 0.45 | -2.05 |
| 11-11 14:16 | +20 | SOL | UP | 0.62 | open |  |
