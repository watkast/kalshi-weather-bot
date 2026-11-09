# Range-Scalp Bot

*Updated Mon Nov 09 22:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53981 | 47082 | 6899 (89) | 5 | $-14754.86 | -4.3% |
| **+10¢** | 40315 | 32266 | 8049 (117) | 7 | $-13729.52 | -5.4% |
| **+15¢** | 33788 | 25112 | 8676 (149) | 7 | $-12508.02 | -5.9% |
| **+20¢** | 30077 | 20976 | 9101 (195) | 8 | $-10972.95 | -5.8% |
| **+10¢ (15¢ stop)** | 65756 | 65646 | 110 (66) | 6 | $-24359.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 22:50 | +10 stop | BNB | DOWN | 0.60 | open |  |
| 11-09 22:50 | +10 stop | ETH | UP | 0.51 | open |  |
| 11-09 22:49 | +10 stop | SOL | UP | 0.53 | open |  |
| 11-09 22:49 | +10 | SOL | UP | 0.53 | open |  |
| 11-09 22:49 | +5 | SOL | UP | 0.53 | 0.60 | 0.35 |
| 11-09 22:49 | +10 stop | DOGE | UP | 0.62 | 0.45 | -2.05 |
| 11-09 22:49 | +10 stop | NEAR | UP | 0.55 | open |  |
| 11-09 22:49 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-09 22:49 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-09 22:49 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-09 22:49 | +10 stop | BTC | DOWN | 0.64 | open |  |
| 11-09 22:49 | +15 | BTC | DOWN | 0.64 | open |  |
| 11-09 22:49 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-09 22:49 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 22:48 | +10 stop | SOL | DOWN | 0.61 | 0.39 | -2.54 |
| 11-09 22:48 | +10 stop | NEAR | DOWN | 0.56 | 0.36 | -2.35 |
| 11-09 22:47 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 11-09 22:47 | +5 | ETH | DOWN | 0.57 | open |  |
| 11-09 22:47 | +5 | HYPE | UP | 0.71 | open |  |
| 11-09 22:47 | +10 stop | DOGE | DOWN | 0.60 | 0.42 | -2.15 |
| 11-09 22:47 | +20 | DOGE | DOWN | 0.60 | open |  |
| 11-09 22:47 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-09 22:47 | +10 | DOGE | DOWN | 0.60 | open |  |
| 11-09 22:47 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-09 22:47 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 11-09 22:47 | +20 | ETH | DOWN | 0.54 | open |  |
| 11-09 22:47 | +15 | ETH | DOWN | 0.54 | open |  |
| 11-09 22:47 | +10 | ETH | DOWN | 0.54 | open |  |
| 11-09 22:47 | +5 | ETH | DOWN | 0.54 | 0.59 | 0.15 |
| 11-09 22:46 | +10 stop | SOL | UP | 0.49 | 0.34 | -1.84 |
| 11-09 22:46 | +20 | SOL | UP | 0.49 | open |  |
| 11-09 22:46 | +15 | SOL | UP | 0.49 | open |  |
| 11-09 22:46 | +10 | SOL | UP | 0.49 | 0.60 | 0.75 |
| 11-09 22:46 | +5 | SOL | UP | 0.49 | 0.60 | 0.75 |
| 11-09 22:46 | +10 stop | BNB | UP | 0.57 | 0.34 | -2.64 |
| 11-09 22:46 | +20 | BNB | UP | 0.57 | open |  |
| 11-09 22:46 | +15 | BNB | UP | 0.57 | open |  |
| 11-09 22:46 | +10 | BNB | UP | 0.57 | open |  |
| 11-09 22:46 | +5 | BNB | UP | 0.57 | open |  |
| 11-09 22:46 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
