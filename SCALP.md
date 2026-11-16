# Range-Scalp Bot

*Updated Mon Nov 16 04:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61686 | 53829 | 7857 (115) | 4 | $-16588.71 | -4.3% |
| **+10¢** | 46079 | 36872 | 9207 (157) | 5 | $-15535.23 | -5.4% |
| **+15¢** | 38609 | 28677 | 9932 (196) | 8 | $-14170.56 | -5.8% |
| **+20¢** | 34418 | 24001 | 10417 (249) | 8 | $-12388.21 | -5.7% |
| **+10¢ (15¢ stop)** | 75065 | 74911 | 154 (90) | 5 | $-27635.24 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 04:19 | +10 stop | BTC | UP | 0.52 | open |  |
| 11-16 04:18 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
| 11-16 04:18 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 11-16 04:18 | +5 | SOL | UP | 0.63 | open |  |
| 11-16 04:18 | +5 | BTC | UP | 0.63 | open |  |
| 11-16 04:18 | +5 | NEAR | UP | 0.69 | open |  |
| 11-16 04:18 | +10 stop | BNB | UP | 0.65 | open |  |
| 11-16 04:18 | +10 | BNB | UP | 0.65 | open |  |
| 11-16 04:17 | +5 | BNB | UP | 0.60 | 0.65 | 0.17 |
| 11-16 04:17 | +10 stop | HYPE | UP | 0.54 | open |  |
| 11-16 04:17 | +20 | HYPE | UP | 0.55 | open |  |
| 11-16 04:17 | +15 | HYPE | UP | 0.55 | open |  |
| 11-16 04:17 | +10 | HYPE | UP | 0.55 | open |  |
| 11-16 04:17 | +5 | HYPE | UP | 0.55 | open |  |
| 11-16 04:17 | +10 stop | SOL | DOWN | 0.60 | 0.43 | -2.03 |
| 11-16 04:17 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-16 04:17 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-16 04:17 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-16 04:17 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 11-16 04:17 | +10 stop | BTC | DOWN | 0.52 | 0.36 | -1.95 |
| 11-16 04:17 | +20 | BTC | DOWN | 0.52 | open |  |
| 11-16 04:17 | +15 | BTC | DOWN | 0.53 | open |  |
| 11-16 04:17 | +10 | BTC | DOWN | 0.53 | open |  |
| 11-16 04:17 | +5 | BTC | DOWN | 0.53 | 0.61 | 0.45 |
| 11-16 04:17 | +10 stop | ZEC | DOWN | 0.47 | open |  |
| 11-16 04:17 | +20 | ZEC | DOWN | 0.47 | open |  |
| 11-16 04:17 | +15 | ZEC | DOWN | 0.48 | open |  |
| 11-16 04:17 | +10 | ZEC | DOWN | 0.48 | open |  |
| 11-16 04:17 | +5 | ZEC | DOWN | 0.48 | 0.55 | 0.34 |
| 11-16 04:16 | +10 stop | BNB | UP | 0.49 | 0.63 | 1.05 |
| 11-16 04:16 | +20 | BNB | UP | 0.49 | 0.69 | 1.67 |
| 11-16 04:16 | +15 | BNB | UP | 0.49 | 0.65 | 1.26 |
| 11-16 04:16 | +10 | BNB | UP | 0.49 | 0.63 | 1.05 |
| 11-16 04:16 | +5 | BNB | UP | 0.49 | 0.54 | 0.14 |
| 11-16 04:16 | +10 stop | ETH | UP | 0.60 | 0.71 | 0.78 |
| 11-16 04:16 | +20 | ETH | UP | 0.59 | open |  |
| 11-16 04:16 | +15 | ETH | UP | 0.59 | open |  |
| 11-16 04:16 | +10 | ETH | UP | 0.59 | 0.71 | 0.88 |
| 11-16 04:16 | +5 | ETH | UP | 0.60 | 0.66 | 0.27 |
| 11-16 04:16 | +10 stop | XRP | UP | 0.62 | open |  |
